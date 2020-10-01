package main

import (
	"image/color"

	"fyne.io/fyne"

	"fmt"
	"strconv"

	"fyne.io/fyne/app"
	"fyne.io/fyne/canvas"
	"fyne.io/fyne/layout"
	"fyne.io/fyne/widget"
)

func main() {
	a := app.New()
	w := a.NewWindow("CALCULADORA 1.0")
	ent1 := widget.NewEntry()
	ent1.Wrapping = fyne.TextWrapWord
	ent2 := widget.NewEntry()
	ent2.Wrapping = fyne.TextWrapWord
	ent3 := widget.NewEntry()
	ent3.Wrapping = fyne.TextWrapWord
	ent4 := widget.NewEntry()
	ent4.Wrapping = fyne.TextWrapWord
	ent5 := widget.NewEntry()
	ent5.Wrapping = fyne.TextWrapWord
	ent6 := widget.NewEntry()
	ent6.Wrapping = fyne.TextWrapWord
	ent7 := widget.NewEntry()
	ent7.Wrapping = fyne.TextWrapWord
	ent8 := widget.NewEntry()
	ent8.Wrapping = fyne.TextWrapWord

	mais := canvas.NewText("+", color.Black)
	mais.Alignment = fyne.TextAlignCenter
	menos := canvas.NewText("-", color.Black)
	menos.Alignment = fyne.TextAlignCenter
	mult := canvas.NewText("*", color.Black)
	mult.Alignment = fyne.TextAlignCenter
	div := canvas.NewText("/", color.Black)
	div.Alignment = fyne.TextAlignCenter
	//mais.Resize(fyne.NewSize(1, 1))

	resul1 := widget.NewLabel("A soma eh: ")
	resul1.Alignment = fyne.TextAlignCenter
	resul2 := widget.NewLabel("A diferenca eh: ")
	resul2.Alignment = fyne.TextAlignCenter
	resul3 := widget.NewLabel("O produto eh: ")
	resul3.Alignment = fyne.TextAlignCenter
	resul4 := widget.NewLabel("O quociente eh: ")
	resul4.Alignment = fyne.TextAlignCenter

	btn := widget.NewButton("calcular", func() {
		str := ent1.Text
		if str == "" || len(str) < 3 {
			//pop := widget.NewPopUp(fyne.NewContainerWithLayout(layout.NewCenterLayout(), canvas.NewText("Error: Number of character invalid!", color.Black)), fyne.)
			//pop.Show()
		}
		n1, err := strconv.ParseFloat(str, 64)
		if err != nil {
			panic(err)
		}
		str2 := ent2.Text
		if str2 == "" {
			panic("Error")
		}
		n2, er := strconv.ParseFloat(str2, 64)
		if er != nil {
			panic(er)
		}
		soma := n1 + n2

		str3 := ent3.Text
		if str3 == "" {
			panic("Error")
		}
		n1, er = strconv.ParseFloat(str3, 64)
		if er != nil {
			panic(er)
		}
		str4 := ent4.Text
		if str4 == "" {
			panic("Error")
		}
		n2, er = strconv.ParseFloat(str4, 64)
		if er != nil {
			panic(er)
		}
		sub := n1 - n2

		str5 := ent5.Text
		if str5 == "" {
			panic("Error")
		}
		n1, er = strconv.ParseFloat(str5, 64)
		if er != nil {
			panic(er)
		}
		str6 := ent6.Text
		if str6 == "" {
			panic("Error")
		}
		n2, er = strconv.ParseFloat(str6, 64)
		if er != nil {
			panic(er)
		}
		mult := n1 * n2

		str7 := ent7.Text
		if str7 == "" {
			panic("Error")
		}
		n1, er = strconv.ParseFloat(str7, 64)
		if er != nil {
			panic(er)
		}
		str8 := ent8.Text
		if str8 == "" {
			panic("Error")
		}
		n2, er = strconv.ParseFloat(str8, 64)
		if er != nil {
			panic(er)
		}
		div := n1 / n2

		resul1.SetText(resul1.Text + fmt.Sprint(soma))
		resul2.SetText(resul2.Text + fmt.Sprint(sub))
		resul3.SetText(resul3.Text + fmt.Sprint(mult))
		resul4.SetText(resul4.Text + fmt.Sprint(div))

	})
	btn.Alignment = widget.ButtonAlignCenter
	//btnsum.Resize(fyne.NewSize(15, 4))

	w.Resize(fyne.NewSize(640, 480))
	w.SetFixedSize(true)
	w.CenterOnScreen()

	content := fyne.NewContainerWithLayout(layout.NewFixedGridLayout(fyne.NewSize(265, 30)), layout.NewSpacer(), fyne.NewContainerWithLayout(layout.NewHBoxLayout(), ent1, mais, ent2), layout.NewSpacer(), fyne.NewContainerWithLayout(layout.NewHBoxLayout(), ent3, menos, ent4), layout.NewSpacer(), fyne.NewContainerWithLayout(layout.NewHBoxLayout(), ent5, mult, ent6), layout.NewSpacer(), fyne.NewContainerWithLayout(layout.NewHBoxLayout(), ent7, div, ent8), fyne.NewContainerWithLayout(layout.NewVBoxLayout(), resul1, resul2, resul3, resul4, btn))
	w.SetContent(content)
	w.ShowAndRun()
}
