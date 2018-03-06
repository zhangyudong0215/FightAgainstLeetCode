func floodFill(image [][]int, sr int, sc int, newColor int) [][]int { // 28ms
    originColor := image[sr][sc]
    if originColor == newColor {
        return image
    }
    fillnewColor(&image, sr, sc, originColor, newColor)
    return image   
}

func fillnewColor(image *[][]int, r, c, originColor, newColor int) {
    if (*image)[r][c] == originColor {
        (*image)[r][c] = newColor
        if r > 0 {
            fillnewColor(image, r-1, c, originColor, newColor)
        }
        if r < len(*image) - 1 {
            fillnewColor(image, r+1, c, originColor, newColor)
        }
        if c > 0 {
            fillnewColor(image, r, c-1, originColor, newColor)
        }
        if c < len((*image)[0]) - 1 {
            fillnewColor(image, r, c+1, originColor, newColor)
        }
    }
}
