import numpy as np
from numpy import array, linalg, matrix
from scipy.special import comb
import cv2
from skimage.morphology import skeletonize
import sknw
import svgwrite

#
# Bézier curve fitting with SciPy
# https://stackoverflow.com/questions/12643079/b%C3%A9zier-curve-fitting-with-scipy
#
Mtk = lambda n, t, k: t**(k)*(1-t)**(n-k)*comb(n,k)
bezierM = lambda ts: matrix([[Mtk(3,t,k) for k in range(4)] for t in ts])

def lsqfit(points, M):
    M_ = linalg.pinv(M)
    return M_ * points

def get_bezier(pts):
    points = array(pts)
    ts = array(range(points.shape[0]), dtype='float')/(points.shape[0]-1)
    M = bezierM(ts)
    control_points = lsqfit(points, M)
    return control_points.tolist()


if __name__ == '__main__':

    fname = 'test'
    src = cv2.imread(fname + '.png', cv2.IMREAD_GRAYSCALE)
    _, src = cv2.threshold(src, 192, 255, cv2.THRESH_BINARY)

    # Skeleton化
    # https://scikit-image.org/docs/dev/auto_examples/edges/plot_skeleton.html
    ske = skeletonize(~(src != 0))
    ske_gray = (ske * 255).astype(np.uint8)
    ske_rgb = cv2.cvtColor(ske_gray, cv2.COLOR_GRAY2RGB)
    cv2.imwrite(fname + '_ske.png', ske_rgb)

    # Skeleton Networkを作成
    # https://github.com/Image-Py/sknw
    graph = sknw.build_sknw(ske.astype(np.uint16), multi=True)

    dwg = svgwrite.Drawing(fname + '.svg', profile='tiny')

    # Edge
    for (s,e) in graph.edges():

        pt_s = graph.node[s]['o'].tolist()
        pt_e = graph.node[e]['o'].tolist()

        for g in graph[s][e].values():

            # 開始 + 中間点 + 終点
            pts = g['pts'].tolist()
            pts = [pt_s] + pts + [pt_e]

            # 点群にフィットするBezierのパラメータを取得
            params = get_bezier(pts)

            # Bezierとして描画
            d = 'M{},{} C{},{} {},{}, {},{}'.format( params[0][0], params[0][1], params[1][0], params[1][1], params[2][0], params[2][1], params[3][0], params[3][1])
            p = dwg.path( d=d, stroke='#000', fill='none', stroke_width=5)
            dwg.add(p)

            # 線をそのまま描画
            #for i in range(len(pts)-1):
            #    dwg.add(dwg.line(pts[i], pts[i+1], stroke='#000', stroke_width=5))

    dwg.save()