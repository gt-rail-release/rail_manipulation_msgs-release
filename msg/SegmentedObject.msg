sensor_msgs/PointCloud2 point_cloud   # Segmented point cloud
sensor_msgs/Image image               # Segmented RGB image
geometry_msgs/Point centroid          # Centroid of the point cloud
geometry_msgs/Quaternion orientation  # Orientation of the object (typically only known for recognized objects)
bool recognized                       # True if the object is recognized
string name                           # Object name (if recognized)
uint32 model_id                       # Object model ID (if recognized)
float64 confidence                    # Recognition confidence value
geometry_msgs/PoseStamped[] grasps    # List of grasp poses (if recognized)
visualization_msgs/Marker marker      # The downsampled visualization of the object

