using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using UnityEngine;
using UnityEngine.UI;
using Debug = UnityEngine.Debug;
using TMPro;
//using static UnityEditor.Timeline.TimelinePlaybackControls;

public class CaptureAndPrint : MonoBehaviour
{
    public string m_ScreenCapturePath = @"C:\Capture\Images\"; // 디렉토리 이름과 파일 이름에 빈칸 없이 생성 
    public string m_ScreenCaptureFilePrefix = "CoderZero"; // 디렉토리 이름과 파일 이름에 빈칸 없이 생성 
    private string m_ScreenCaptureFilePath;

    public RawImage display;
    WebCamTexture camTexture;
    private int currentIndex = 0;

    public float xPos;
    public float yPos;

    //240112
    private int count = 3;
    //public TextMeshProUGUI count_Text;
    public GameObject countText;
    Coroutine countCoroutine;
    public ScreenConvertManager screenConvertManager;
    public Canvas screenCanvas;
    public GameObject picture_Captured;

    private int count_OnAddSticker = 30;
    public GameObject countText_OnAddSticker;
    Coroutine count_OnAddSticker_Coroutine;
    public GameObject Page04_01;
    public GameObject Page04_02;
    public EraseAllStickers eraseAllStickers;

    public RectTransform captured_Picture_RectTransform;

    public GameObject printPicturePage;
    public GameObject waitingPrintPage;
    public TypeEffect typingEffect;

    public AudioSource audioSource;
    public AudioClip takePicktureSoundEffect;
    public AudioClip buttonClickSoundEffect;
    

    private void Start()
    {
        Application.targetFrameRate = 30;

        WebCamDevice device = WebCamTexture.devices[currentIndex];
        camTexture = new WebCamTexture(device.name);
        display.texture = camTexture;
        camTexture.Play();

        //audioSource.clip = takePicktureSoundEffect;
    }

    void Update()
    {
        /*
        // 캡처 후 저장 
        if (Input.GetKeyDown(KeyCode.F11))
        {
            //Capture(m_ScreenCapturePath, m_ScreenCaptureFilePrefix);
            StartCoroutine( SaveImage() );
        }

        // 프린트 
        if (Input.GetKeyDown(KeyCode.F12))
        {
            Print(m_ScreenCaptureFilePath);
        }
        */
    }

    IEnumerator SaveImage()
    {
        Debug.Log("사진을 저장합니다.");
        yield return new WaitForEndOfFrame();

        Texture2D screenTex = new Texture2D((int)display.rectTransform.sizeDelta.x, (int)display.rectTransform.sizeDelta.y, TextureFormat.RGB24, false);
        //Texture2D screenTex = new Texture2D((int)display.rectTransform.sizeDelta.x, (int)display.rectTransform.sizeDelta.y - 50, TextureFormat.RGB24, false);

        Rect area = new Rect(xPos, yPos, display.rectTransform.sizeDelta.x, display.rectTransform.sizeDelta.y);
        screenTex.ReadPixels(area, 0, 0);

        if (Directory.Exists(m_ScreenCapturePath) == false)
        {
            Directory.CreateDirectory(m_ScreenCapturePath);
        }

        m_ScreenCaptureFilePath = m_ScreenCapturePath + m_ScreenCaptureFilePrefix + DateTime.Now.ToString("yyyyMMddhhmmss") + ".png";

        File.WriteAllBytes(m_ScreenCaptureFilePath, screenTex.EncodeToPNG());

        //240112
        byte[] textureInfo = File.ReadAllBytes(m_ScreenCaptureFilePath);
        screenTex.LoadImage(textureInfo);

        Rect rect = new Rect(0, 0, screenTex.width, screenTex.height);
        Sprite pictureSprite = Sprite.Create(screenTex, rect, Vector2.one * 0.5f);

        picture_Captured.GetComponent<Image>().sprite = pictureSprite;

        //audioSource.Play();

        //Invoke("CallNextPage", 1f);

        // destroy하지 않으면 어떻게 되는지? >> 촬영/재촬영/스티커추가 하는데에 문제는 없음, destroy하면 재촬영때 이미지 생성이 안됨
        //Destroy(screenTex);
    }

    //void CallNextPage()
    //{
    //    screenConvertManager.NextPage();
    //}

    //public void Click_Print()
    //{
    //    StartCoroutine(SaveImage());
    //}



    public Texture2D ToTexture2D(Texture texture)
    {
        return Texture2D.CreateExternalTexture(
            texture.width,
            texture.height,
            TextureFormat.RGB24,
            false, false,
            texture.GetNativeTexturePtr());
    }

    void Capture(string filePath, string filePrefix = "")
    {
        // ① 캡처 후 저장 할 디렉토리가 존재하지 않으면 디렉토리 생성 
        DirectoryInfo directoryInfo = new DirectoryInfo(filePath);

        if (!directoryInfo.Exists)
        {
            directoryInfo.Create();
        }

        // ② 캡처 
        m_ScreenCaptureFilePath = filePath + filePrefix + DateTime.Now.ToString("yyyyMMddhhmmss") + ".png";
        ScreenCapture.CaptureScreenshot(m_ScreenCaptureFilePath);
    }

    void Print(string filePath)
    {
        string printerName = "Canon SELPHY CP1500"; //본인 인쇄기 이름 HP OfficeJet Pro 8210 PCL-6
        string fullCommand = "rundll32 C:\\WINDOWS\\system32\\shimgvw.dll,ImageView_PrintTo " + "\"" + filePath + "\"" + " " + "\"" + printerName + "\"";
        PrintImage(fullCommand);
    }
    void PrintImage(string _cmd)
    {
        try
        {
            Process myProcess = new Process();
            //외부 프로그램 숨김 상태
            //myProcess.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            myProcess.StartInfo.CreateNoWindow = true;
            myProcess.StartInfo.UseShellExecute = false;
            myProcess.StartInfo.FileName = "cmd.exe";
            myProcess.StartInfo.Arguments = "/c " + _cmd;
            myProcess.EnableRaisingEvents = true;
            myProcess.Start();
            myProcess.WaitForExit();
        }
        catch (Exception e)
        {
            UnityEngine.Debug.Log(e);
        }

    }

    //240111
    public void Click_PrintPicture()
    {
        Debug.Log("사진을 출력합니다.");
        Click_TakePictureOnAddSticker();
        Print(m_ScreenCaptureFilePath);
        StartCoroutine(BeforePrintPictureAction());
    }

    IEnumerator BeforePrintPictureAction()
    {
        yield return new WaitForSeconds(0.1f);
        printPicturePage.SetActive(false);
        waitingPrintPage.SetActive(true);
        typingEffect.Click_TypingEffect();
    }

    public void Click_SaveImageOnEndCountDown()
    {
        StartCoroutine(SaveImageOnEndCountDown());
    }

    IEnumerator CountDown()
    {
        yield return new WaitForSeconds(1.0f);
        count--;

        if (count > 0)
        {
            countText.GetComponent<TextMeshProUGUI>().text = count.ToString();
            countCoroutine = StartCoroutine(CountDown());
        }
        else
        {
            StopCoroutine(countCoroutine);
            countText.SetActive(false);
            count = 3;
            countText.GetComponent<TextMeshProUGUI>().text = count.ToString();

            // Save Image OnEnd CountDown
            StartCoroutine(SaveImage());
        }
    }

    IEnumerator SaveImageOnEndCountDown()       
    {
        countText.SetActive(true);
        StartCoroutine(CountDown());
        yield return new WaitForSeconds(3f);
        StartCoroutine(SaveImage());
        audioSource.clip = takePicktureSoundEffect;
        audioSource.Play();
        yield return new WaitForSeconds(1f);
        screenConvertManager.NextPage();
        // 사진 촬영시 변경되는 카메라 렌더모드 돌려놓기 >> 렌더모드 바꾸던 스크립트 삭제해서 굳이 필요 없을듯함.
        // screenCanvas.renderMode = RenderMode.ScreenSpaceOverlay;
    }




    public void Click_TakePictureOnAddSticker() // 테스트용 함수
    {
        StartCoroutine(BeforePrintPictureAction());
        StartCoroutine(SaveImage());
    }


    IEnumerator CountDown_OnAddSticker()
    {
        yield return new WaitForSeconds(1.0f);
        count_OnAddSticker--;

        if (count_OnAddSticker > 0)
        {
            countText_OnAddSticker.GetComponent<TextMeshProUGUI>().text = count_OnAddSticker.ToString();
            count_OnAddSticker_Coroutine = StartCoroutine(CountDown_OnAddSticker());
        }
        else
        {
            StopCoroutine(count_OnAddSticker_Coroutine);
            countText_OnAddSticker.SetActive(false);
            count_OnAddSticker = 30;
            countText_OnAddSticker.GetComponent<TextMeshProUGUI>().text = count_OnAddSticker.ToString();

            // 화면에 등록된 스티커 초기화
            eraseAllStickers.DestroyAllStickers();

            // 화면 초기화
            Page04_01.SetActive(true);
            Page04_02.SetActive(false);
            screenConvertManager.currentPageIndex = 0;
            screenConvertManager.ShowCurrentPage();
            Click_CapturedPictureMoveToStartPoint();
        }
    }

    public void Click_CountDown_OnAddSticker()
    {
        StartCoroutine(CountDown_OnAddSticker());
    }

    public void Click_StopCountDown_OnAddSticker()
    {
        StopCoroutine(count_OnAddSticker_Coroutine);

        // 카운트 초기화
        count_OnAddSticker = 30;
        countText_OnAddSticker.GetComponent<TextMeshProUGUI>().text = count_OnAddSticker.ToString();
    }

    public void Click_CapturedPictureMoveToStartPoint()
    {
        Debug.Log("시작 지점으로 이동했습니다.");
        captured_Picture_RectTransform.anchoredPosition = new Vector2(0, -20);
    }

    public void Click_CapturedPictureMoveToAddStickerPoint()
    {
        Debug.Log("스티커 부착 지점으로 이동했습니다.");
        captured_Picture_RectTransform.anchoredPosition = new Vector2(-350, -20);
    }

    public void Click_ButtonSound()
    {
        audioSource.clip = buttonClickSoundEffect;
        audioSource.Play();
    }

    public void Click_SaveImage()
    {
        StartCoroutine(SaveImage());
    }
}
