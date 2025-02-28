import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import cv2

class facecode():

    base_face_encoding = np.load('known_face_encodings.npy')
    print(base_face_encoding)
    with open("known_face_names.txt", 'r') as f:
        known_face_names = [line.rstrip('\n') for line in f]
    # Create arrays of known face encodings and their names
    print(type(known_face_names[0]))
    known_face_encodings = base_face_encoding
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    def faceplot(frame):
        print("running")
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if facecode.process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            facecode.face_locations = face_recognition.face_locations(rgb_small_frame)
            facecode.face_encodings = face_recognition.face_encodings(rgb_small_frame, facecode.face_locations)
            print("processing")
            facecode.face_names = []
            for facecode.face_encoding in facecode.face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(facecode.known_face_encodings, facecode.face_encoding)
                name = "Unknown"

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = facecode.known_face_names[first_match_index]

                facecode.face_names.append(name)

        facecode.process_this_frame = not facecode.process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(facecode.face_locations, facecode.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        #cv2.imshow('Video', frame)
        return (frame)
