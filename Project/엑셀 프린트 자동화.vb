Sub IncrementPrint()
'updateby Extendoffice
    Dim xCount As Variant
    Dim xScreen As Boolean
    Dim I As Long
    On Error Resume Next
LInput:
    xCount = Application.InputBox("Please enter the number of copies you want to print:", "Kutools for Excel")
    If TypeName(xCount) = "Boolean" Then Exit Sub
    If (xCount = "") Or (Not IsNumeric(xCount)) Or (xCount < 1) Then
        MsgBox "error entered, please enter again", vbInformation, "Kutools for Excel"
        GoTo LInput
    Else
        xScreen = Application.ScreenUpdating
        Application.ScreenUpdating = False
        For I = 1 To xCount
            ActiveSheet.Range("A1").Value = " Company-00" & I
            ActiveSheet.PrintOut
        Next
        ActiveSheet.Range("A1").ClearContents
        Application.ScreenUpdating = xScreen
    End If
End Sub