import cv2
import mediapipe as mp
import serial
import time
import speech_recognition as sr
import pyttsx3
import keyboard

import threading
r = sr.Recognizer()
text=""
text1=""
text2=""
text3=""
flag=0
flag1=True
thumb_status = 0
index_status = 0
middle_status = 0
ring_status = 0
pinky_status = 0
x = 0
status = 0
var=False

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


def speaktext(command):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.say(command)
    engine.runAndWait()
def listening_func():
    global text3  # Declare text3 as a global variable
    text3=""
    with sr.Microphone() as source:
        speaktext("which mode do you prefer")
        print("Listen for command...")
        try:
            r.adjust_for_ambient_noise(source, duration=2)
            speaktext("now you can speak")
            print("speak....")
            audio = r.listen(source, timeout=4)
            text3=text = r.recognize_google(audio)

            text = text.lower()
            print("You said:", text)
            if "camera" in text or "voice" in text:
                speaktext("The mode has been selected successfully ")
            else:
                speaktext("the mode is not selected successfully select camera or voice")
        except sr.WaitTimeoutError:
            print("No speech detected. Please speak again.")
            speaktext("No speech detected. Please speak again.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            speaktext("Sorry, I could not understand what you said.")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
def toggle_modes():

    global var
    global text3
    global cap
    if var == True:
        text3="voice"
        var=not var
    elif var == False:
        text3 = "camera"
        cap = cv2.VideoCapture(0)
       # speaktext("please press escape to continue when camera be opened")
        var = not var


def listening_func2():
    global text2
    with sr.Microphone() as source:
        speaktext("which command do you prefer")
        print("Listen for command...")
        try:
            r.adjust_for_ambient_noise(source, duration=2)
            speaktext("now you can speak")
            print("speak....")
            audio = r.listen(source, timeout=4)
            text2 = r.recognize_google(audio)

            text2 = text2.lower()
            print("You said:", text2)
            return text2
        except sr.WaitTimeoutError:
            print("No speech detected. Please speak again.")
            speaktext("No speech detected. Please speak again.")

            return ""
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            speaktext("Sorry, I could not understand what you said.")

            return ""

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""
ser = serial.Serial(port="COM5", baudrate=9600)

speaktext("bluetooth is connected successfully. please press t to select the mode ")

#text3="camera"
 while True:
      if keyboard.is_pressed('t'):
       listening_func()
      if "camera" in text3 or "voice" in text3:
         break

print("the mode is :")
print(text3)
#keyboard.clear_all_hotkeys()
keyboard.is_pressed('t')


if "camera" in text3:
    cap = cv2.VideoCapture(0)
    var=True
    flag=1
    print("Camera mode selected")
else:
    var=False
    print("voice mode  selected")

#keyboard.add_hotkey('t',toggle_modes)


# Open the camera
mp_drawing= mp.solutions.drawing_utils
x=0
def fire_toggle():
    global var
    while True:
     if keyboard.read_key() == 't':
        toggle_modes()
        time.sleep(0.1)  # Add a small delay to avoid CPU hogging
# Create a thread
#my_thread = threading.Thread(target=fire_toggle)
# Start the thread
#my_thread.start()
v=0
start_time = time.time()

while True:

 current_time = time.time()

 if keyboard.is_pressed('t') and v==0:
     toggle_modes()
     speaktext("the mode is changed please press escape to continue")
     while True:
      if keyboard.is_pressed('esc'):
       break

 print(var)
 print(text3)
 if "camera" in text3 :

    finger_status = []
    flag1=True

      #ser.close()
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to read a frame from the camera")
        continue

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = mp_hands.process(frame_rgb)

    # Check if hands are detected
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:
            # Create an array to store the finger status


            # Get the landmarks for the hand
            landmarks = hand_landmarks.landmark

            # Get the y-coordinate of each fingertip
            index_tip_y = landmarks[8].y
            middle_tip_y = landmarks[12].y
            ring_tip_y = landmarks[16].y
            pinky_tip_y = landmarks[20].y
            thumb_tip_x = landmarks[4].x

            index_closed=0
            middle_closed=0
            ring_closed=0
            pinky_closed=0
            thumb_closed=0
            # Determine if fingers are open or closed based on the y-coordinate of each fingertip
          #  index_closed = index_tip_y > landmarks[5].y
          #  middle_closed = middle_tip_y > landmarks[9].y
          #  ring_closed = ring_tip_y > landmarks[13].y
          #  pinky_closed = pinky_tip_y > landmarks[17].y
          #  thumb_closed = thumb_tip_x > landmarks[2].x
            if index_tip_y > landmarks[5].y:
                index_closed=180
            if middle_tip_y > landmarks[9].y:
                middle_closed=180
            if ring_tip_y > landmarks[13].y :
                 ring_closed=180
            if pinky_tip_y > landmarks[17].y:
                pinky_closed=180
            if thumb_tip_x > landmarks[1].x:
                thumb_closed=180

            if index_tip_y > landmarks[7].y and index_tip_y < landmarks[5].y:
                index_closed = 90
            if middle_tip_y > landmarks[11].y and  middle_tip_y < landmarks[9].y:
                middle_closed = 90
            if ring_tip_y > landmarks[15].y and ring_tip_y < landmarks[13].y:
                ring_closed = 90
            if pinky_tip_y > landmarks[19].y and pinky_tip_y < landmarks[17].y:
                pinky_closed = 90
            if thumb_tip_x > landmarks[3].x and thumb_tip_x < landmarks[2].x:
                thumb_closed = 90
            # Assign 1 if the finger is closed, otherwise assign 0
            thumb_status = thumb_closed
            index_status = index_closed
            middle_status = middle_closed
            ring_status = ring_closed
            pinky_status = pinky_closed

            # Append the finger status to the array
            if landmarks[5].x >landmarks[17].x:
                if thumb_status==90 or thumb_status==180:
                     thumb_status=0
                x=180

            elif format(landmarks[5].x,".1f") == format(landmarks[17].x,".1f"):
                if thumb_status == 90 or thumb_status == 180:
                    thumb_status = 0
                x = 90
            else:
                x=0
            finger_status.extend([thumb_status, index_status, middle_status, ring_status, pinky_status,x])
        #    binary_string = ''.join(map(str, finger_status))
         #   decimal_number = int(binary_string, 2)
         #   decimal_number_as_int = int(decimal_number)
           # send_to_atmega(decimal_number_as_int)
            #send_to_atmega(x)
           # ser.write(bytearray(finger_status))
            # Display the finger status in the console
           # print(str(finger_status).encode())

        # print(f"tip :{landmarks[0].y}")
    # Display the resulting frame
    if current_time - start_time >= 0.50 :
        print(f"Finger Status: {finger_status}")

        ser.write(str(finger_status).encode())
        ser.flush()
        start_time += 0.5  # Increment start_time by 1 second


    cv2.imshow('Hand Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 elif "voice" in text3 :
     finger_status=[]
     if flag==1:
         cap.release()
         cv2.destroyAllWindows()
     if flag1== True:
         speaktext("press c key to tell the command you want")
         flag1= not flag1
     while True:
        if keyboard.is_pressed('c')  :
         text2 = listening_func2()
         break
        if keyboard.is_pressed('t') and v == 0:
            toggle_modes()
            speaktext("the mode is changed ")
            break
     print(text2)
     if "close" in text2:
         status = 180
         if "one" in text2 or "1" in text2:
             thumb_status = status
         if "two" in text2 or "2" in text2:
             index_status = status
         if "three" in text2 or "3" in text2:
             middle_status = status
         if "four" in  text2 or "4" in text2:
             ring_status = status
         if "five" in text2 or "5" in text2:
             pinky_status = status
     elif "open" in text2:
         status1 = 0
         if "one" in text2 or "1" in text2:
             thumb_status = status1
         if "two" in text2 or "2" in text2:
             index_status = status1
         if "three" in text2 or "3" in text2:
             middle_status = status1
         if "four" in text2 or "4" in text2:
             ring_status = status1
         if "five" in text2  or "5" in text2:
             pinky_status = status1
     finger_status.extend([thumb_status, index_status, middle_status, ring_status, pinky_status, x])
     print(finger_status)
     ser.write(str(finger_status).encode())

# Release the capture and destroy any open windo

cap.release()
cv2.destroyAllWindows()