import cv2
import numpy as np
import os



def main():

    # Reading the original image
    org_img = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/INIAD_logo.png")
    hsv = cv2.cvtColor(org_img, cv2.COLOR_BGR2HSV)

    # Spliting to H,S,V
    h_img, s_img, v_img = cv2.split(hsv)
    s_img = cv2.bitwise_not(s_img)

    # Flattening a histgram of s_img
    hist_s_img = cv2.equalizeHist(s_img)

    # Binarization
    _, result_bin = cv2.threshold(
        s_img, 200, 255, cv2.THRESH_BINARY)

    # Morphing（Closing）
    ## Setting filters
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (4, 4))
    ## Execution morphing
    result_morphing = cv2.morphologyEx(
        result_bin, cv2.MORPH_CLOSE, kernel)

    # Detection contours
    contours, _ = cv2.findContours(
        result_morphing, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Contour approximation
    approx = approx_contour(contours)

    # Contour line drawing
    cp_org_img_for_draw = np.copy(org_img)
    drawing_edge(org_img, approx, cp_org_img_for_draw)

    # Setting for display
    setting_for_display()
    # Execution display
    display_result(
        org_img, h_img, s_img, v_img, hist_s_img,
        result_bin, result_morphing, cp_org_img_for_draw)

def approx_contour(contours):
    ######################################################
    # 輪郭直線近似
    ######################################################
    approx = []
    for i in range(len(contours)):
        cnt = contours[i]
        epsilon = 0.0001*cv2.arcLength(cnt,True)
        approx.append(cv2.approxPolyDP(cnt,epsilon,True))
    return approx


def drawing_edge(org_img, contours, cp_org_img_for_draw):
    ######################################################
    # 輪郭線描画
    ######################################################
    min_area = 100
    large_contours = [
        cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    cv2.drawContours(cp_org_img_for_draw, large_contours, -1, (255, 0, 0), 5)


def setting_for_display():
    ######################################################
    # 表示設定
    # 概要: imshow()で表示する際のウィンドウをサイズ変更可能にする設定
    ######################################################

    # 元画像
    cv2.namedWindow('org_img', cv2.WINDOW_NORMAL)
    cv2.namedWindow("h", cv2.WINDOW_NORMAL)
    cv2.namedWindow("s", cv2.WINDOW_NORMAL)
    cv2.namedWindow("v", cv2.WINDOW_NORMAL)

    # # Hヒストグラム平坦化後
    cv2.namedWindow('hist_s_img', cv2.WINDOW_NORMAL)

    # 二値化
    cv2.namedWindow('result_bin', cv2.WINDOW_NORMAL)

    # モーフィング
    cv2.namedWindow('result_morphing', cv2.WINDOW_NORMAL)

    # 輪郭線描画
    cv2.namedWindow('cp_org_img_for_draw', cv2.WINDOW_NORMAL)


def display_result(
        org_img, h_img, s_img, v_img, hist_s_img,
        result_bin, result_morphing, cp_org_img_for_draw):
    ######################################################
    # 表示処理
    ######################################################

    # 元画像
    cv2.imshow('org_img', org_img)
    cv2.imshow("h", h_img)
    cv2.imshow("s", s_img)
    cv2.imshow("v", v_img)

    # Hヒストグラム平坦化後
    cv2.imshow('hist_s_img', hist_s_img)

    # 二値化
    cv2.imshow('result_bin', result_bin)

    # モーフィング
    cv2.imshow('result_morphing', result_morphing)

    # 輪郭線描画
    cv2.imshow('cp_org_img_for_draw', cp_org_img_for_draw)

    # 入力待機（これがないとimshow()の表示がされないため注意）
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
