## node_detector_control

### Services

* detector_control_node/add_object_detector
  * Used to add models for detection
    * name (string)
    * model_path (string)
    * label_path (string)
* detector_control_node/remove_object_detector
  * Used to remove models added with add_object_detector
    * name (string), same that was given with add_object_detector
* detector_control_node/filter_by
  * Used for filtering observations. Default value is false.
    * enabled (bool) Enable or disable filtering
    * filter_by_field (string) The ROS msg field to filter by (class_id, label, observation_type)
    * include (string[]) Array containing the values as strings to keep. All others will be filtered out
* detector_control_node/sort_by
  * Used to sort by field in ascending order. Default is false and then detections are sorted by TFlite detector in descending order.
    * sort_by (string) The name of the ROS msg field to sort by.
* combine_toggle
  * Toggle the combining of observations from all detectors to a single Ros message
    * state (bool)
* [detector_name]/frequency
  * Changes the rate of image processing of the specified detector to the received frequency in hz
    * frequency (int32)
  * Replies with a new_frequencyResponse (string) after the rate has been changed
* [detector_name]/toggle
  * Toggles detections with the specified detector
    * state (bool)

* detector_control_node/labels
  * returns a list of the objects current detectors can recognise
  	* labels (string array)
      
### Topics

* observations, observations from all active detectors are published here
    * metadata (string), JSON-formatted string containing miscellaneous info of the observations. Current detectors use the following:
      * camera_id, identifier for the video source
      * image_counter, identifier for the frame
      * image_height and image_width, image dimensions
      * active_detectors, list of currently used detectors
      * skipped_detectors, list of detectors that were skipped due to the rate limit

    * observations (observation array)
      * observation_type (string), name of the detector used, "QR" for QR
      * class_id (uint16) class_id given by Tensorflow, 65535 for QR-detections
      * label (string) mapped to label file with class_id, QR-detector sets the name of the detector (currently QR)
      * score (float64) confidence score between 0.0-1.0 from Tensorflow or 1 from QR-detector
      * data (string) data from observations, currently only QR-detector sets the data read from QR-code, Tensorflow leaves empty
      * bbox (bbox), bounds of rectangle around the detected object/QR code. Values between 0.0-1.0, offset from top left corner
        * top (float64)
        * right (float64)
        * bottom (float64)
        * left (float64)
      * pol (polygon), more accurate bound for QR observations
        * length (uint8), amount of points
        * points (point64 array), values between 0.0-1.0, offset from top left corner
          * y (float64)
          * x (float64)
* warning, sent when detection takes longer than desired rate
  * message (string)
  
### Ros-parameters

Different detectors can be set up on startup via a 2d dictionary of dictionaries containing parameter entry, for an example:

\<param name="init_detectors" type="yaml" value="{object_detect: {model_path: 'ssd_mobilenet_v1_1_metadata_1.tflite', label_path: 'mscoco_complete_labels', detect_on: True, frequency: 42}, QR: {detect_on: True, frequency: 5}}" /\>


Which results in an object-detection node with the name "object_detect" and an qr-detection with the name "QR". For every key in the outer dictionary, the dictionary in node_detection_control.py:s constructor must contain the same key with an suitable class as value.

Only name, model_path and label_path are required, frequency and detect_on have default values set in the detector-classes.


## node_camera

### Topics

* camera/images, continuously published frames from the assigned video source as Ros image messages
  * camera_id (string) 
  * image_counter (uint64), identifier for the frames
  * data (uint8 array), the three color channels as a one dimensional byte array
  * height (uint16), height of the image in pixels
  * width (uint16), width of the image in pxels
  
### Parameters

* video_source (string), path to the device or file to publish video from

## Program structure

![](https://raw.githubusercontent.com/Konenako/Ohtuprojekti-kesa2020/master/documentation/program_structure.png "Program structure")

