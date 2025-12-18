# Module 1: The Robotic Nervous System (ROS 2)

## Module 1: The Robotic Nervous System (ROS 2)

### Middleware for Robot Control

Welcome to Module 1, where we embark on an exciting journey into the world of Robotic Operating System 2 (ROS 2). In this module, we'll delve into ROS 2, a powerful open-source framework that serves as the backbone for developing sophisticated robotic applications. Think of ROS 2 as the "nervous system" of your robot, enabling different components to communicate, process information, and execute actions seamlessly.

#### Learning Objectives:

Upon successful completion of this module, you will be able to:

1.  **Understand ROS 2 architecture:** Grasp the fundamental building blocks and design principles of ROS 2.
2.  **Master ROS 2 Nodes, Topics, and Services:** Comprehend and utilize the core communication paradigms: nodes for computational units, topics for asynchronous data streams, and services for synchronous request-response interactions.
3.  **Learn to bridge Python Agents to ROS controllers using `rclpy`:** Understand how to integrate your Python-based Artificial Intelligence (AI) agents with ROS 2 for robot control.
4.  **Understand URDF for humanoids:** Learn about the Unified Robot Description Format (URDF) and its importance in describing the physical characteristics and kinematic structure of robots, particularly humanoids.

---

### 1. Introduction to ROS 2

Robots are complex systems, involving a multitude of sensors, actuators, processing units, and algorithms working in concert. Managing this complexity and facilitating communication between these disparate components is a significant challenge. This is where middleware comes in, and ROS 2 stands out as a leading solution in the robotics domain.

**What is Middleware?**

Middleware is software that acts as an intermediary between different applications or software components. In the context of robotics, it provides a standardized way for robots to:

*   **Communicate:** Exchange data between different parts of the robot (e.g., sensor readings to processing algorithms, commands to actuators).
*   **Manage Processes:** Organize and run various computational tasks.
*   **Share Information:** Make data and functionality accessible to different applications and developers.
*   **Facilitate Development:** Offer tools and libraries to speed up the development process.

**Why ROS 2?**

ROS 1, the predecessor to ROS 2, revolutionized robotics development. However, it had limitations in areas like real-time performance, security, and multi-robot systems. ROS 2 was designed from the ground up to address these shortcomings, offering:

*   **Improved Real-time Capabilities:** Better suited for time-critical robotic applications.
*   **Enhanced Security:** Built-in security features for robust communication.
*   **Support for Embedded Systems and Microcontrollers:** Can run on a wider range of hardware.
*   **Multi-robot System Support:** Designed for coordinating multiple robots.
*   **Cross-Platform Compatibility:** Runs on Linux, macOS, and Windows.
*   **Modernized Communication:** Utilizes the Data Distribution Service (DDS) as its underlying communication layer, providing flexibility and reliability.

**ROS 2 Architecture - A High-Level View**

At its core, ROS 2 is a collection of tools, libraries, and conventions that simplify the task of creating complex robot behavior across a wide range of robotic platforms. It operates on a distributed system model, meaning different parts of your robot's software can run on different computers or even different robots, all communicating seamlessly.

The key components of the ROS 2 architecture are:

*   **Nodes:** The fundamental processing units in ROS 2. A node is typically a single executable that performs a specific task, such as reading a sensor, controlling a motor, or running a navigation algorithm.
*   **Topics:** Named buses over which nodes exchange messages. Think of them as communication channels. A node can publish (send) messages to a topic, and other nodes can subscribe (receive) messages from that topic. This is a one-to-many communication pattern.
*   **Services:** A mechanism for synchronous, request-response communication between nodes. One node acts as a service server, offering a specific function, while another node acts as a service client, requesting that function and waiting for a response. This is a one-to-one communication pattern.
*   **Actions:** Similar to services but designed for long-running tasks that may require feedback during execution and can be preempted.
*   **Parameters:** Allow you to configure nodes at runtime without recompiling.
*   **Launch Files:** Scripts that allow you to start and configure multiple nodes and their relationships.

This module will focus on the fundamental building blocks: Nodes, Topics, and Services.

---

### 2. ROS 2 Core Concepts: Nodes, Topics, Services

Let's dive deeper into the essential elements that form the backbone of ROS 2 communication.

#### 2.1 Nodes

As mentioned, **Nodes** are the individual processes that perform specific functions within your robotic system. Imagine a robot's software being broken down into these manageable, independent units.

*   **Examples of Nodes:**
    *   A camera driver node that publishes image data.
    *   A motor controller node that receives velocity commands and actuates motors.
    *   A SLAM (Simultaneous Localization and Mapping) node that processes sensor data to build a map and determine the robot's position.
    *   A path planning node that calculates a route for the robot.

*   **Key Characteristics of Nodes:**
    *   **Independent Executables:** Each node is typically a separate program.
    *   **Communication:** Nodes communicate with each other using topics, services, and actions.
    *   **Resource Management:** Each node manages its own resources (CPU, memory).

#### 2.2 Topics

**Topics** are the primary mechanism for asynchronous communication in ROS 2. They allow nodes to exchange data in a publish-subscribe model.

*   **Publishers:** A node that sends data (publishes) to a specific topic.
*   **Subscribers:** A node that receives data (subscribes) from a specific topic.

*   **How it Works:**
    1.  A node (publisher) creates a message and sends it to a designated topic.
    2.  Any other node (subscriber) that has registered interest in that topic will receive the message.
    3.  There can be multiple publishers on a single topic, and multiple subscribers to a single topic. This makes it a one-to-many communication pattern.

*   **Message Types:** Data exchanged over topics are encapsulated in **messages**. ROS 2 defines various standard message types (e.g., for sensor readings, commands, status updates) and allows you to define your own custom message types.

*   **Example Scenario:**
    *   A **Lidar sensor node** publishes distance measurements to a topic named `/scan`.
    *   A **obstacle avoidance node** subscribes to `/scan` to get the Lidar data and process it to avoid collisions.
    *   A **mapping node** also subscribes to `/scan` to build a map of the environment.

#### 2.3 Services

**Services** provide a synchronous request-response communication mechanism. This is useful when a node needs to request a specific action or computation from another node and must wait for the result before continuing.

*   **Service Server:** A node that offers a specific service. It listens for incoming requests and performs the requested operation.
*   **Service Client:** A node that calls a service. It sends a request to the service server and waits for a response.

*   **How it Works:**
    1.  A node (client) sends a request to a specific service.
    2.  The service server receives the request, performs the operation, and sends a response back to the client.
    3.  The client receives the response and can then proceed.
    4.  This is typically a one-to-one communication pattern.

*   **Service Types:** Similar to messages, services have defined **service types**, which specify the structure of the request and response.

*   **Example Scenario:**
    *   A **navigation service server** is running, capable of calculating a path between two points.
    *   A **user interface node** (client) wants to send the robot to a specific location. It calls the navigation service, providing the start and end coordinates as the request.
    *   The navigation service server computes the path and returns it as a response to the UI node. The UI node can then visualize or command the robot to follow this path.

---

### 3. ROS 2 Installation and Setup

To begin working with ROS 2, you need to install it on your system. We'll focus on installing ROS 2 Humble Hawksbill, a Long-Term Support (LTS) release, which is recommended for most projects due to its stability and extended support period.

**Prerequisites:**

*   A supported Linux distribution (Ubuntu is highly recommended).
*   Internet connection.

**Installation Steps (for Ubuntu):**

**Step 1: Enable the Universe Repository**

```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository universe
```

**Step 2: Add the ROS 2 Humble Repository**

```bash
sudo curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
```

**Step 3: Update Your Package Index and Install ROS 2**

```bash
sudo apt update
sudo apt install ros-humble-desktop
```

*   `ros-humble-desktop` includes the core ROS 2 libraries, command-line tools, and common packages like `rqt`, `rviz`, and `rosbag`.
*   For a minimal installation (just the core libraries and command-line tools), you can use `ros-humble-ros-base`.

**Step 4: Sourcing the ROS 2 Environment**

After installation, you need to "source" the ROS 2 setup files so that your shell knows where to find the ROS 2 commands and libraries. You'll need to do this every time you open a new terminal.

```bash
source /opt/ros/humble/setup.bash
```

**Step 5: Verify Installation**

You can verify the installation by running a simple ROS 2 command:

```bash
ros2 --version
```

This should output the ROS 2 version (e.g., `2.30.1`).

**Setting up for Persistent Use (Optional but Recommended)**

To avoid manually sourcing the setup file every time, you can add it to your shell's configuration file (e.g., `~/.bashrc` for Bash shell):

1.  Open your `.bashrc` file in a text editor:
    ```bash
    nano ~/.bashrc
    ```
2.  Add the following line at the end of the file:
    ```bash
    source /opt/ros/humble/setup.bash
    ```
3.  Save and close the file.
4.  Apply the changes to your current terminal session:
    ```bash
    source ~/.bashrc
    ```
    Now, every new terminal you open will have the ROS 2 environment sourced automatically.

---

### 4. Creating Your First ROS 2 Package

ROS 2 projects are organized into **packages**. A package is a directory that contains ROS 2 code (nodes), launch files, configuration files, message/service definitions, and other related assets.

**Package Structure:**

A typical ROS 2 package has the following structure:

```
my_package/
├── CMakeLists.txt
├── package.xml
├── src/
│   └── my_package/
│       └── __init__.py
│       └── my_node.py
└── launch/
    └── my_launch_file.launch.py
```

*   `CMakeLists.txt`: Used for building C++ packages.
*   `package.xml`: Contains metadata about the package (name, version, author, dependencies).
*   `src/`: Directory for your Python or C++ source code.
*   `launch/`: Directory for ROS 2 launch files.

**Creating a New Package:**

1.  **Navigate to your ROS 2 workspace's `src` directory.** If you don't have a workspace yet, you'll need to create one:
    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    ```
    *   `ros2_ws` is a common name for a ROS 2 workspace.

2.  **Use the `ros2 pkg create` command to generate a new package.**
    Let's create a package named `my_robot_pkg` that will contain Python nodes.

    ```bash
    ros2 pkg create --build-type ament_python my_robot_pkg
    ```

    *   `--build-type ament_python`: Specifies that this package will be built using Python. For C++, you would use `ament_cmake`.

    This command will create the `my_robot_pkg` directory with the basic structure and essential files.

**Understanding `package.xml`:**

Open `~/ros2_ws/src/my_robot_pkg/package.xml` in a text editor. It will look something like this:

```xml
<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
  <name>my_robot_pkg</name>
  <version>0.0.0</version>
  <description>TODO: Package description</description>
  <maintainer email="user@todo.com">user</maintainer>
  <license>TODO: License declaration</license>

  <exec_depend>rclpy</exec_depend>
  <exec_depend>std_msgs</exec_depend>

  <test_depend>ament_copyright</test_depend>
  <test_depend>ament_flake8</test_depend>
  <test_depend>ament_pep257</test_depend>
  <test_depend>python3-pytest</test_depend>

  <export>
    <build_type>ament_python</build_type>
  </export>
</package>
```

*   **`<name>`:** The name of your package.
*   **`<version>`:** The version of your package.
*   **`<description>`:** A brief description of your package.
*   **`<maintainer>`:** Information about the package maintainer.
*   **`<license>`:** The license under which your package is distributed.
*   **`<exec_depend>`:** Specifies dependencies that are required at runtime. Here, `rclpy` is the Python client library for ROS 2, and `std_msgs` is a package containing standard ROS message types.
*   **`<export>`:** Declares the build type.

**Building Your Workspace:**

After creating or modifying packages, you need to build your workspace to make them available to ROS 2.

1.  Navigate to the root of your workspace:
    ```bash
    cd ~/ros2_ws
    ```
2.  Build the workspace:
    ```bash
    colcon build
    ```
    *   `colcon` is the build tool used by ROS 2. It understands how to build packages based on their build types (e.g., `ament_python`, `ament_cmake`).

3.  **Source the workspace's setup file.** This makes your newly built packages available in your current terminal session:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```
    *   Again, for persistent use, add this line to your `~/.bashrc` file.

Now, ROS 2 should be aware of your `my_robot_pkg`. You can check this by running:

```bash
ros2 pkg list
```

You should see `my_robot_pkg` in the list.

---

### 5. Publisher-Subscriber Pattern

The Publisher-Subscriber (Pub/Sub) pattern is the cornerstone of asynchronous data exchange in ROS 2. It allows nodes to communicate without direct knowledge of each other.

**Core Components:**

*   **Topic:** A named channel for messages.
*   **Publisher:** A node that sends messages to a topic.
*   **Subscriber:** A node that receives messages from a topic.
*   **Message:** The data structure transmitted over a topic.

**Creating a Simple Publisher Node:**

Let's create a simple publisher that sends a counter value every second.

1.  Navigate to your package's source directory:
    ```bash
    cd ~/ros2_ws/src/my_robot_pkg/my_robot_pkg/
    ```
2.  Create a new Python file named `simple_publisher.py`.
3.  Paste the following code into `simple_publisher.py`:

    ```python
    import rclpy
    from rclpy.node import Node

    from std_msgs.msg import String # We'll use a simple String message for now

    class SimplePublisher(Node):

        def __init__(self):
            # Initialize the node with a name
            super().__init__('simple_publisher')
            # Create a publisher for the 'chatter' topic with String message type
            self.publisher_ = self.create_publisher(String, 'chatter', 10)
            # Set a timer to call the timer_callback function every 1 second
            timer_period = 1.0  # seconds
            self.timer = self.create_timer(timer_period, self.timer_callback)
            self.counter = 0

        def timer_callback(self):
            # Create a String message
            msg = String()
            msg.data = f'Hello ROS 2: {self.counter}'
            # Publish the message
            self.publisher_.publish(msg)
            # Log the published message
            self.get_logger().info(f'Publishing: "{msg.data}"')
            # Increment the counter
            self.counter += 1

    def main(args=None):
        # Initialize the ROS 2 Python client library
        rclpy.init(args=args)
        # Create an instance of our SimplePublisher node
        simple_publisher = SimplePublisher()
        # Spin the node so the callback functions are called
        rclpy.spin(simple_publisher)
        # Destroy the node explicitly
        simple_publisher.destroy_node()
        # Shutdown the ROS 2 Python client library
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```

**Explanation of the Publisher Code:**

*   `import rclpy`, `from rclpy.node import Node`: Imports necessary ROS 2 Python modules.
*   `from std_msgs.msg import String`: Imports the `String` message type from the `std_msgs` package.
*   `class SimplePublisher(Node):`: Defines a class that inherits from `rclpy.node.Node`.
*   `super().__init__('simple_publisher')`: Initializes the base `Node` class and gives our node the name `simple_publisher`.
*   `self.publisher_ = self.create_publisher(String, 'chatter', 10)`:
    *   `String`: The type of message to be published.
    *   `'chatter'`: The name of the topic.
    *   `10`: The Quality of Service (QoS) history depth. It determines how many messages are queued if the subscriber isn't ready to receive them.
*   `self.timer = self.create_timer(timer_period, self.timer_callback)`: Creates a timer that will call `self.timer_callback` every `timer_period` seconds.
*   `self.timer_callback(self)`: This method is executed by the timer.
    *   `msg = String()`: Creates a new `String` message object.
    *   `msg.data = f'Hello ROS 2: {self.counter}'`: Sets the actual data within the message.
    *   `self.publisher_.publish(msg)`: Publishes the message to the 'chatter' topic.
    *   `self.get_logger().info(...)`: Logs an informational message to the console.
*   `main(args=None)`: The main entry point for the node.
    *   `rclpy.init(args=args)`: Initializes the ROS 2 Python client.
    *   `simple_publisher = SimplePublisher()`: Creates an instance of our publisher node.
    *   `rclpy.spin(simple_publisher)`: Keeps the node alive and processing callbacks (like our timer). It will block until the node is shut down.
    *   `simple_publisher.destroy_node()`: Cleans up the node resources.
    *   `rclpy.shutdown()`: Shuts down the ROS 2 client library.

**Creating a Simple Subscriber Node:**

Now, let's create a subscriber to listen to the 'chatter' topic.

1.  In the same directory (`~/ros2_ws/src/my_robot_pkg/my_robot_pkg/`), create a new Python file named `simple_subscriber.py`.
2.  Paste the following code into `simple_subscriber.py`:

    ```python
    import rclpy
    from rclpy.node import Node

    from std_msgs.msg import String

    class SimpleSubscriber(Node):

        def __init__(self):
            # Initialize the node with a name
            super().__init__('simple_subscriber')
            # Create a subscriber for the 'chatter' topic with String message type
            # When a message is received, the listener_callback function will be called
            self.subscription = self.create_subscription(
                String,
                'chatter',
                self.listener_callback,
                10)
            self.subscription  # Prevent unused variable warning

        def listener_callback(self, msg):
            # Log the received message
            self.get_logger().info(f'I heard: "{msg.data}"')

    def main(args=None):
        # Initialize the ROS 2 Python client library
        rclpy.init(args=args)
        # Create an instance of our SimpleSubscriber node
        simple_subscriber = SimpleSubscriber()
        # Spin the node so the callback functions are called
        rclpy.spin(simple_subscriber)
        # Destroy the node explicitly
        simple_subscriber.destroy_node()
        # Shutdown the ROS 2 Python client library
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```

**Explanation of the Subscriber Code:**

*   `self.subscription = self.create_subscription(...)`:
    *   `String`: The type of message to expect.
    *   `'chatter'`: The name of the topic to subscribe to.
    *   `self.listener_callback`: The function that will be called whenever a message arrives on the topic.
    *   `10`: The QoS history depth, matching the publisher.
*   `self.listener_callback(self, msg)`: This method is executed whenever a `String` message is received on the 'chatter' topic. The received message is passed as the `msg` argument.
*   `self.get_logger().info(f'I heard: "{msg.data}"')`: Logs the content of the received message.

**Running the Publisher and Subscriber:**

1.  **Build your workspace** if you haven't already after adding the new files:
    ```bash
    cd ~/ros2_ws
    colcon build
    ```
2.  **Source your workspace's setup file** in a *new* terminal:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```
3.  **Launch the subscriber node:**
    ```bash
    ros2 run my_robot_pkg simple_subscriber
    ```
    You should see output indicating the node has started.

4.  **In another *new* terminal**, **source your workspace's setup file** and **launch the publisher node:**
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 run my_robot_pkg simple_publisher
    ```
    You should see output in the publisher's terminal indicating it's publishing messages. In the subscriber's terminal, you should see output like:
    ```
    [INFO] [simple_subscriber]: I heard: "Hello ROS 2: 0"
    [INFO] [simple_subscriber]: I heard: "Hello ROS 2: 1"
    ...
    ```

**Inspecting Topics with `ros2 topic`:**

ROS 2 provides command-line tools to inspect the ROS 2 graph.

*   **List all active topics:**
    ```bash
    ros2 topic list
    ```
    You should see `/chatter` and `/rosout` (a system topic).

*   **Describe a topic:**
    ```bash
    ros2 topic info /chatter
    ```
    This will show the message type and which nodes are publishing and subscribing to it.

*   **Echo a topic:**
    ```bash
    ros2 topic echo /chatter
    ```
    This command will print all messages published to the `/chatter` topic. You can run this in a separate terminal to see the messages being sent by the publisher without running the subscriber node.

---

### 6. Service-Client Pattern

The Service-Client pattern enables synchronous communication, where a client requests a service from a server and waits for a response. This is ideal for tasks that require a definite outcome before proceeding.

**Core Components:**

*   **Service Server:** A node that provides a specific service.
*   **Service Client:** A node that calls a service and waits for a response.
*   **Service Type:** Defines the structure of the request and response messages.

**Defining a Custom Service Type:**

For this example, we'll create a simple service that takes two integers and returns their sum.

1.  **Create a new directory for custom messages and services within your package.**
    ```bash
    mkdir ~/ros2_ws/src/my_robot_pkg/my_robot_pkg/srv
    ```
2.  **Create a service definition file.** Let's call it `AddTwoInts.srv`.
    ```bash
    nano ~/ros2_ws/src/my_robot_pkg/my_robot_pkg/srv/AddTwoInts.srv
    ```
3.  Paste the following content into `AddTwoInts.srv`:

    ```
    int64 a
    int64 b
    ---
    int64 sum
    ```

    *   The lines before `---` define the **request** part of the service (two `int64` integers named `a` and `b`).
    *   The lines after `---` define the **response** part of the service (an `int64` integer named `sum`).

4.  **Modify `CMakeLists.txt` to find and build the service.**
    Open `~/ros2_ws/src/my_robot_pkg/CMakeLists.txt` and add the following lines:

    ```cmake
    # Find the ament_cmake_core package
    find_package(ament_cmake_core REQUIRED)

    # Add the package to the CMake build system
    ament_package()

    # --- Add these lines for service generation ---
    find_package(rosidl_default REQUIRED)
    rosidl_generate_interfaces(${PROJECT_NAME}
      "srv/AddTwoInts.srv"
    )
    # --------------------------------------------
    ```

5.  **Modify `package.xml` to add dependencies.**
    Open `~/ros2_ws/src/my_robot_pkg/package.xml` and add the following `build_depend`, `exec_depend`, and `member_of_group` tags within the `<package>` tags:

    ```xml
    <build_depend>rosidl_default_generators</build_depend>
    <exec_depend>rosidl_default_runtime</exec_depend>
    <member_of_group>rosidl_interface_packages</member_of_group>
    ```

**Creating a Service Server Node:**

1.  Create a new Python file named `add_two_ints_server.py` in `~/ros2_ws/src/my_robot_pkg/my_robot_pkg/`.
2.  Paste the following code:

    ```python
    import rclpy
    from rclpy.node import Node

    # Import the custom service message
    from my_robot_pkg.srv import AddTwoInts

    class AddTwoIntsServer(Node):

        def __init__(self):
            super().__init__('add_two_ints_server')
            # Create a service server
            # Parameters: service type, service name, callback function, QoS profile
            self.srv = self.create_service(
                AddTwoInts,  # The custom service type
                'add_two_ints', # The name of the service
                self.add_two_ints_callback) # The function to call when a request is received
            self.get_logger().info('Add two integers service ready.')

        def add_two_ints_callback(self, request, response):
            # request is an object containing the request data (a and b)
            # response is an object to populate with the response data (sum)

            self.get_logger().info(f'Incoming request: a={request.a} b={request.b}')

            # Perform the calculation
            response.sum = request.a + request.b

            # Log and return the response
            self.get_logger().info(f'Returning response: {response.sum}')
            return response

    def main(args=None):
        rclpy.init(args=args)
        add_two_ints_server = AddTwoIntsServer()
        rclpy.spin(add_two_ints_server)
        add_two_ints_server.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```

**Creating a Service Client Node:**

1.  Create a new Python file named `add_two_ints_client.py` in `~/ros2_ws/src/my_robot_pkg/my_robot_pkg/`.
2.  Paste the following code:

    ```python
    import sys
    import rclpy
    from rclpy.node import Node

    # Import the custom service message
    from my_robot_pkg.srv import AddTwoInts

    class AddTwoIntsClient(Node):

        def __init__(self):
            super().__init__('add_two_ints_client')
            # Create a client for the 'add_two_ints' service
            # Parameters: service type, service name, QoS profile
            self.cli = self.create_client(AddTwoInts, 'add_two_ints')
            # Wait until the service is available. This is important for services.
            while not self.cli.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('Service not available, waiting again...')
            # Create a request object
            self.req = AddTwoInts.Request()

        def send_request(self, a, b):
            # Set the request data
            self.req.a = a
            self.req.b = b
            # Call the service asynchronously
            self.future = self.cli.call_async(self.req)
            # Keep spinning until the future (response) is complete
            rclpy.spin_until_future_complete(self, self.future)
            # Return the response
            return self.future.result()

    def main(args=None):
        rclpy.init(args=args)

        # Get command line arguments for a and b
        if len(sys.argv) != 3:
            print('Usage: ros2 run my_robot_pkg add_two_ints_client <int1> <int2>')
            sys.exit(1)

        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
        except ValueError:
            print('Please provide valid integers for a and b.')
            sys.exit(1)

        add_two_ints_client = AddTwoIntsClient()
        response = add_two_ints_client.send_request(a, b)

        if response:
            add_two_ints_client.get_logger().info(
                f'Request: a={a} b={b} | Response: sum={response.sum}')
        else:
            add_two_ints_client.get_logger().error('Service call failed')

        add_two_ints_client.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```

**Running the Service-Client Pair:**

1.  **Build your workspace** to include the service definition and new nodes:
    ```bash
    cd ~/ros2_ws
    colcon build
    ```
2.  **Source your workspace's setup file** in a *new* terminal:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```
3.  **Launch the service server node:**
    ```bash
    ros2 run my_robot_pkg add_two_ints_server
    ```
    You should see "Add two integers service ready."

4.  **In another *new* terminal**, **source your workspace's setup file** and **launch the service client node with arguments:**
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 run my_robot_pkg add_two_ints_client 5 7
    ```
    The client will send a request to the server with `a=5` and `b=7`. The server will calculate the sum, and the client will print the result.

    You should see output like:
    ```
    [INFO] [add_two_ints_client]: Request: a=5 b=7 | Response: sum=12
    ```
    In the server's terminal, you'll see:
    ```
    [INFO] [add_two_ints_server]: Incoming request: a=5 b=7
    [INFO] [add_two_ints_server]: Returning response: 12
    ```

**Inspecting Services with `ros2 service`:**

*   **List all available services:**
    ```bash
    ros2 service list
    ```
    You should see `/add_two_ints`.

*   **Describe a service:**
    ```bash
    ros2 service list /add_two_ints
    ```
    This will show the service type.

*   **Call a service (for testing):**
    ```bash
    ros2 service call /add_two_ints my_robot_pkg/srv/AddTwoInts "{a: 10, b: 20}"
    ```
    This is a powerful command for testing services directly from the command line.

---

### 7. URDF for Humanoid Robots

**URDF (Unified Robot Description Format)** is an XML format used to describe the physical structure, kinematics, and visual properties of a robot. It's crucial for robotics applications because it allows for:

*   **Kinematic Modeling:** Defining the relationships between different parts of the robot (links) and how they connect (joints). This is essential for motion planning and simulation.
*   **Visualization:** Describing how the robot should be rendered in simulation environments like RViz.
*   **Collision Detection:** Specifying collision meshes for physics-based simulations.
*   **Sensor and Actuator Information:** Defining the properties of attached sensors and actuators.

**Key Concepts in URDF:**

*   **`<robot name="...">`:** The root element, defining the name of the robot.
*   **`<link>`:** Represents a rigid body (e.g., a leg segment, a torso, a hand). Each link has a name and can contain:
    *   **`<visual>`:** Defines how the link is rendered (geometry, material).
    *   **`<collision>`:** Defines the collision geometry for physics simulation.
    *   **`<inertial>`:** Defines the mass and inertia properties for physics simulation.
*   **`<joint>`:** Defines the relationship between two links, allowing for relative motion. Joints have types (e.g., `revolute` for rotation, `prismatic` for linear motion, `fixed` for no motion). They also have names and specify parent and child links.

**URDF for Humanoids:**

Humanoid robots are particularly complex due to their bipedal locomotion, articulated limbs, and often a head and torso. URDF plays a vital role in describing:

*   **Legs:** Multiple joints (hip, knee, ankle) for each leg.
*   **Torso:** Waist and neck joints for rotation and bending.
*   **Arms:** Shoulder, elbow, and wrist joints for each arm.
*   **Hands:** Multiple degrees of freedom for gripping.
*   **Head:** Neck and possibly eye joints for looking around.

**Example Snippet (Simplified Humanoid Torso):**

```xml
<robot name="humanoid_simple">
  <link name="base_link">
    <!-- Base of the robot, typically the pelvis -->
    <visual>
      <geometry>
        <box size="0.3 0.2 0.4"/>
      </geometry>
      <origin xyz="0 0 0.2"/>
    </visual>
  </link>

  <link name="torso">
    <!-- The main body -->
    <visual>
      <geometry>
        <box size="0.3 0.2 0.5"/>
      </geometry>
      <origin xyz="0 0 0.5"/>
    </visual>
  </link>

  <joint name="base_to_torso" type="fixed">
    <!-- Fixed joint connecting base_link to torso -->
    <parent link="base_link"/>
    <child link="torso"/>
    <origin xyz="0 0 0.4"/> <!-- Position of torso relative to base_link -->
  </joint>

  <link name="neck">
    <!-- Neck joint and head base -->
    <visual>
      <geometry>
        <sphere radius="0.1"/>
      </geometry>
      <origin xyz="0 0 0.1"/>
    </visual>
  </link>

  <joint name="torso_to_neck" type="revolute">
    <!-- Revolute joint for neck pitch -->
    <parent link="torso"/>
    <child link="neck"/>
    <origin xyz="0 0 1.0"/> <!-- Position of neck relative to torso -->
    <axis xyz="1 0 0"/> <!-- Pitch axis -->
    <limit lower="-0.785" upper="0.785" velocity="1.0" effort="1.0"/>
  </joint>

  <link name="head">
    <!-- The head -->
    <visual>
      <geometry>
        <sphere radius="0.2"/>
      </geometry>
      <origin xyz="0 0 0.2"/>
    </visual>
  </link>

  <joint name="neck_to_head" type="fixed">
    <!-- Fixed joint connecting neck to head -->
    <parent link="neck"/>
    <child link="head"/>
    <origin xyz="0 0 0.2"/> <!-- Position of head relative to neck -->
  </joint>

</robot>
```

**Practical Component: Building a URDF Model of a Simple Robot**

For this module, we'll focus on creating a URDF for a very simple robot to understand the structure. A full humanoid URDF is extensive.

1.  Create a new package for URDF, or add to your `my_robot_pkg`. Let's create a new package:
    ```bash
    cd ~/ros2_ws/src
    ros2 pkg create --build-type ament_cmake simple_robot_description
    ```
2.  Create a `urdf` directory inside the new package:
    ```bash
    mkdir ~/ros2_ws/src/simple_robot_description/urdf
    ```
3.  Create a URDF file named `simple_robot.urdf` inside the `urdf` directory.
    ```bash
    nano ~/ros2_ws/src/simple_robot_description/urdf/simple_robot.urdf
    ```
4.  Paste the following URDF content (a simple arm with a base):

    ```xml
    <?xml version="1.0"?>
    <robot name="simple_arm">

      <!-- Base Link -->
      <link name="base_link">
        <visual>
          <geometry>
            <cylinder length="0.1" radius="0.1"/>
          </geometry>
          <origin rpy="0 0 0" xyz="0 0 0.05"/>
          <material name="blue">
            <color rgba="0 0 1 1"/>
          </material>
        </visual>
        <collision>
          <geometry>
            <cylinder length="0.1" radius="0.1"/>
          </geometry>
          <origin rpy="0 0 0" xyz="0 0 0.05"/>
        </collision>
        <inertial>
          <mass value="1.0"/>
          <origin rpy="0 0 0" xyz="0 0 0.05"/>
          <inertia ixx="0.01" ixy="0.0" ixz="0.0" iyy="0.01" iyz="0.0" izz="0.01"/>
        </inertial>
      </link>

      <!-- Shoulder Joint -->
      <joint name="shoulder_joint" type="revolute">
        <parent link="base_link"/>
        <child link="upper_arm_link"/>
        <origin rpy="0 0 0" xyz="0 0 0.1"/>
        <axis rpy="0 0 0" xyz="0 1 0"/> <!-- Rotate around Y-axis -->
        <limit lower="-1.57" upper="1.57" velocity="1.0" effort="10"/>
      </joint>

      <!-- Upper Arm Link -->
      <link name="upper_arm_link">
        <visual>
          <geometry>
            <box size="0.4 0.05 0.05"/>
          </geometry>
          <origin rpy="0 0 0" xyz="0.2 0 0"/>
          <material name="red">
            <color rgba="1 0 0 1"/>
          </material>
        </visual>
        <collision>
          <geometry>
            <box size="0.4 0.05 0.05"/>
          </geometry>
          <origin rpy="0 0 0" xyz="0.2 0 0"/>
        </collision>
        <inertial>
          <mass value="0.5"/>
          <origin rpy="0 0 0" xyz="0.2 0 0"/>
          <inertia ixx="0.001" ixy="0.0" ixz="0.0" iyy="0.001" iyz="0.0" izz="0.001"/>
        </inertial>
      </link>

      <!-- Elbow Joint -->
      <joint name="elbow_joint" type="revolute">
        <parent link="upper_arm_link"/>
        <child link="forearm_link"/>
        <origin rpy="0 0 0" xyz="0.4 0 0"/>
        <axis rpy="0 0 0" xyz="0 1 0"/> <!-- Rotate around Y-axis -->
        <limit lower="-2.09" upper="2.09" velocity="1.0" effort="10"/>
      </joint>

      <!-- Forearm Link -->
      <link name="forearm_link">
        <visual>
          <geometry>
            <box size="0.3 0.04 0.04"/>
          </geometry>
          <origin rpy="0 0 0" xyz="0.15 0 0"/>
          <material name="green">
            <color rgba="0 1 0 1"/>
          </material>
        </visual>
        <collision>
          <geometry>
            <box size="0.3 0.04 0.04"/>
          </geometry>
          <origin rpy="0 0 0" xyz="0.15 0 0"/>
        </collision>
        <inertial>
          <mass value="0.3"/>
          <origin rpy="0 0 0" xyz="0.15 0 0"/>
          <inertia ixx="0.001" ixy="0.0" ixz="0.0" iyy="0.001" iyz="0.0" izz="0.001"/>
        </inertial>
      </link>

    </robot>
    ```
5.  **Configure the build system.**
    *   Open `~/ros2_ws/src/simple_robot_description/CMakeLists.txt`.
    *   Ensure `ament_package()` is present.
    *   Add the following lines to ensure URDF files are installed correctly:

    ```cmake
    # Add this block to CMakeLists.txt to install URDF files
    install(DIRECTORY urdf
      DESTINATION share/${PROJECT_NAME}
    )
    ```

6.  **Build your workspace:**
    ```bash
    cd ~/ros2_ws
    colcon build
    ```
7.  **Source your workspace's setup file** in a *new* terminal:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```
8.  **View the URDF model using RViz:**
    RViz is a powerful 3D visualization tool for ROS. You can load your URDF model into RViz to see how it renders.

    *   Run RViz:
        ```bash
        rviz2
        ```
    *   In RViz, click "File" -> "Open Config" and navigate to an existing configuration (e.g., a default one) or create a new one.
    *   In the "Displays" panel, click "Add" (+) and select "RobotModel".
    *   In the "RobotModel" properties, under "Robot Description", you should see a "Topic" or "Param Name" field. Click the dropdown and select "/robot_description".
    *   To load your URDF, you need to publish it to a ROS parameter. You can do this using the `robot_state_publisher` node.

    **Create a launch file to load and display the URDF:**

    *   Create a `launch` directory in `~/ros2_ws/src/simple_robot_description/`:
        ```bash
        mkdir ~/ros2_ws/src/simple_robot_description/launch
        ```
    *   Create a launch file named `display_robot.launch.py`:
        ```bash
        nano ~/ros2_ws/src/simple_robot_description/launch/display_robot.launch.py
        ```
    *   Paste the following Python code into the launch file:

        ```python
        import os
        from ament_index_python.packages import get_package_share_directory
        from launch import LaunchDescription
        from launch_ros.actions import Node

        def generate_launch_description():
            # Get the path to the URDF file
            robot_desc_path = os.path.join(
                get_package_share_directory('simple_robot_description'),
                'urdf',
                'simple_robot.urdf'
            )

            # Load the URDF file into the parameter server
            # This node publishes the URDF to the /robot_description topic
            robot_state_publisher_node = Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                name='robot_state_publisher',
                output='screen',
                parameters=[{'use_sim_time': False,  # Set to True if using a simulator
                             'robot_description': open(robot_desc_path).read()}]
            )

            # RViz configuration file (optional, but good for initial setup)
            # You might need to create a default rviz config for this robot
            # For now, we'll launch RViz and let the user add the RobotModel display
            rviz_node = Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                output='screen',
                arguments=['-d', os.path.join(get_package_share_directory('simple_robot_description'), 'rviz', 'default.rviz')]
            )

            return LaunchDescription([
                robot_state_publisher_node,
                # rviz_node # Uncomment if you have a default.rviz file
            ])
        ```
    *   You'll need to create a `rviz` directory and a `default.rviz` file within `simple_robot_description` if you want to uncomment the `rviz_node` line. For now, just launching RViz manually and adding the RobotModel is sufficient.

9.  **Run the launch file:**
    ```bash
    ros2 launch simple_robot_description display_robot.launch.py
    ```
    This will start the `robot_state_publisher` which publishes your URDF to `/robot_description`.
    Then, open `rviz2` in a *separate* terminal, add the "RobotModel" display, and set its "Robot Description" parameter to `/robot_description`. You should see your simple arm rendered.

---

### 8. ROS 2 Control System

The ROS 2 Control System provides a standardized framework for controlling robot hardware. It separates the concerns of real-time control loops from higher-level planning and command generation.

**Key Components:**

*   **Controllers:** Nodes that execute specific control strategies (e.g., position controller, velocity controller).
*   **Controller Manager:** A central node responsible for loading, unloading, starting, and stopping controllers.
*   **Hardware Interface:** An abstraction layer that allows ROS 2 Control to interact with the robot's hardware (sensors and actuators) without knowing the specific details of the hardware implementation.
*   **ROS 2 Control Generic Interface:** Provides a standardized way for controllers to access hardware states and command hardware efforts/positions/velocities.

**How it Works:**

1.  A **hardware interface** is implemented for the robot's actuators and sensors. This interface exposes the desired state variables (e.g., joint position, velocity) and command variables (e.g., joint effort, position command).
2.  A **controller manager** loads and manages various **controllers**.
3.  Each **controller** is configured to interact with specific **hardware interface** state and command variables. For example, a `joint_position_controller` will read the current joint position from the hardware interface and command a new target position.
4.  The **controller manager** and **controllers** typically run in a real-time loop (often using `rt` kernel patches and dedicated hardware/software configurations for guaranteed timing).
5.  Higher-level nodes (e.g., a motion planner) send commands to the controllers via ROS 2 topics or services, and the controllers translate these commands into low-level hardware actions.

**Example Flow:**

*   **Motion Planner (e.g., `moveit2`)**: Wants to move arm to pose X.
*   **Motion Planner publishes a goal pose to a ROS topic.**
*   **A Trajectory Controller (ROS 2 Control)** subscribes to this topic.
*   **Trajectory Controller generates a series of joint commands (positions, velocities, efforts).**
*   **Controller Manager passes these commands to the appropriate Joint Controllers.**
*   **Joint Controllers (e.g., `joint_trajectory_controller`, `joint_velocity_controller`) interact with the Hardware Interface.**
*   **Hardware Interface** sends commands to motors/actuators.
*   **Sensors** report current states back to the **Hardware Interface**.
*   **Hardware Interface** publishes current joint states (position, velocity) on a ROS topic.

**Relevance to Humanoids:**

For humanoid robots, the ROS 2 Control System is crucial for:

*   **Precise Motor Control:** Ensuring smooth and accurate movements of legs, arms, and torso.
*   **Balance and Stability:** Implementing real-time feedback control loops for maintaining balance.
*   **Coordination of Multiple Joints:** Managing the complex interplay of many joints for locomotion and manipulation.
*   **Safety:** Implementing safety limits and emergency stops through the control system.

While implementing a full ROS 2 Control system for a complex humanoid is beyond the scope of this introductory module, understanding its existence and purpose is vital. You would typically find pre-built ROS 2 Control configurations for specific robot platforms or develop custom hardware interfaces.

---

### 9. Integration with Python AI Agents

One of the most powerful aspects of ROS 2 is its ability to integrate with various programming languages, especially Python, for implementing AI and machine learning algorithms.

**Bridging Python Agents to ROS Controllers using `rclpy`:**

`rclpy` is the Python client library for ROS 2. It provides the tools necessary for Python scripts to act as ROS 2 nodes, enabling them to:

*   **Subscribe to sensor data:** Receive information from cameras, lidar, IMUs, etc.
*   **Publish commands to actuators:** Send desired velocities, positions, or trajectories to robot hardware.
*   **Call ROS services:** Request computations or actions from other ROS nodes.
*   **Implement AI algorithms:** Process sensor data, make decisions, and generate control commands.

**How Python Agents Integrate:**

1.  **ROS Node Wrapper:** Your Python AI agent's logic is encapsulated within a ROS 2 node. This node uses `rclpy` to interact with the ROS 2 ecosystem.
2.  **Data Ingestion:** The node subscribes to relevant ROS topics to receive sensor data. For example, an AI agent for object detection might subscribe to a camera topic (`/image_raw`).
3.  **Decision Making:** The AI agent processes the ingested data using its algorithms (e.g., a YOLO model for object detection).
4.  **Action Generation:** Based on its decisions, the AI agent generates commands. For a robot moving towards an object, this might be a desired linear and angular velocity.
5.  **Command Publishing:** The ROS node publishes these generated commands to appropriate ROS topics that are subscribed to by ROS 2 Control nodes or low-level motor controllers.

**Practical Component: Connecting ROS 2 with Python Script**

Let's create a simple example where a Python script acts as an AI agent. It will "decide" to send a specific command based on a simple condition.

We'll reuse our `simple_publisher` and `simple_subscriber` for this. We'll create a new Python "agent" node that subscribes to the `chatter` topic, and if it hears a specific message, it will publish a command to a new topic.

1.  **Create a new Python file `ai_agent.py` in `~/ros2_ws/src/my_robot_pkg/my_robot_pkg/`.**
2.  Paste the following code:

    ```python
    import rclpy
    from rclpy.node import Node

    from std_msgs.msg import String
    from geometry_msgs.msg import Twist # A common message type for velocity commands

    class AIAgent(Node):

        def __init__(self):
            super().__init__('ai_agent')

            # Subscriber to receive messages from the publisher
            self.subscription = self.create_subscription(
                String,
                'chatter',
                self.chatter_callback,
                10)
            self.subscription  # prevent unused variable warning

            # Publisher to send commands (e.g., velocity)
            self.command_publisher = self.create_publisher(Twist, 'robot_command', 10)

            self.get_logger().info('AI Agent is ready. Waiting for "Hello ROS 2: 5" to send command...')

        def chatter_callback(self, msg):
            self.get_logger().info(f'Agent heard: "{msg.data}"')

            # Simple AI decision logic: if we hear a specific message, send a command
            if msg.data == 'Hello ROS 2: 5':
                self.get_logger().info('Triggered AI action! Sending movement command.')
                twist_msg = Twist()
                twist_msg.linear.x = 0.5  # Move forward at 0.5 m/s
                twist_msg.angular.z = 0.0 # No turning
                self.command_publisher.publish(twist_msg)
                self.get_logger().info(f'Published Twist message: linear.x={twist_msg.linear.x}')

    def main(args=None):
        rclpy.init(args=args)
        ai_agent = AIAgent()
        rclpy.spin(ai_agent)
        ai_agent.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```

3.  **Create another Python node that will act as a dummy "robot controller"** to receive and print the commands published by the AI agent. Create `dummy_controller.py` in the same directory.
4.  Paste the following code:

    ```python
    import rclpy
    from rclpy.node import Node

    from geometry_msgs.msg import Twist

    class DummyController(Node):

        def __init__(self):
            super().__init__('dummy_controller')
            # Subscriber to receive commands from the AI Agent
            self.subscription = self.create_subscription(
                Twist,
                'robot_command',
                self.command_callback,
                10)
            self.subscription  # prevent unused variable warning
            self.get_logger().info('Dummy controller is ready. Waiting for robot commands...')

        def command_callback(self, msg):
            self.get_logger().info(f'Received command: Linear.x={msg.linear.x}, Angular.z={msg.angular.z}')
            # In a real robot, this would send commands to motors/actuators

    def main(args=None):
        rclpy.init(args=args)
        dummy_controller = DummyController()
        rclpy.spin(dummy_controller)
        dummy_controller.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```

5.  **Update `my_robot_pkg`'s `package.xml`** to include `geometry_msgs`:
    ```xml
    <exec_depend>geometry_msgs</exec_depend>
    ```
    (Add this line alongside `rclpy` and `std_msgs`).

6.  **Build your workspace:**
    ```bash
    cd ~/ros2_ws
    colcon build
    ```
7.  **Source your workspace's setup file** in a *new* terminal:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```
8.  **Launch the publisher node** (from Section 5):
    ```bash
    ros2 run my_robot_pkg simple_publisher
    ```
    This node will publish messages to `/chatter`.

9.  **In another *new* terminal**, **source your workspace's setup file** and **launch the AI agent:**
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 run my_robot_pkg ai_agent
    ```
    The agent will now subscribe to `/chatter`.

10. **In a third *new* terminal**, **source your workspace's setup file** and **launch the dummy controller:**
    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 run my_robot_pkg dummy_controller
    ```
    This controller will subscribe to `/robot_command`.

**Observation:**

Watch the terminals. The `simple_publisher` will output messages. When its counter reaches `5`, the `ai_agent` will detect the message "Hello ROS 2: 5", print that it's sending a command, and publish a `Twist` message to `/robot_command`. The `dummy_controller` will then receive this `Twist` message and print it.

This demonstrates how a Python script can act as an intelligent agent, consuming data from ROS, making decisions, and publishing commands that other ROS nodes (like controllers) can use.

---

### 10. Practical Examples and Exercises

This section provides hands-on exercises to solidify your understanding of ROS 2 concepts.

**Exercise 1: Simple Publisher-Subscriber Communication**

1.  **Objective:** Create two nodes: one publishing random numbers and another subscribing to these numbers and printing their average.
2.  **Tasks:**
    *   Create a new ROS 2 package (e.g., `number_publisher_subscriber`).
    *   Implement a publisher node that publishes `std_msgs.msg.Float64` messages to a topic named `/random_numbers` at a rate of 2 Hz.
    *   Implement a subscriber node that subscribes to `/random_numbers`, keeps a running sum and count of received numbers, and prints the average every 10 seconds.
    *   Run both nodes and verify they communicate correctly.
    *   Use `ros2 topic list`, `ros2 topic info`, and `ros2 topic echo` to inspect the communication.

**Exercise 2: Custom Service for Robot State**

1.  **Objective:** Create a service that allows a client to request the current battery level of a robot.
2.  **Tasks:**
    *   Define a new service type (e.g., `GetBatteryLevel.srv`) with an empty request and a response containing a `float32` for battery level.
    *   Create a service server node that simulates a battery level (e.g., starting at 100.0 and gradually decreasing).
    *   Create a service client node that calls the `GetBatteryLevel` service and prints the returned battery level.
    *   Configure your package to build the custom service.
    *   Run the server and client and test the service.

**Exercise 3: URDF Viewer for a Simple Gripper**

1.  **Objective:** Create a URDF description for a simple two-finger gripper and visualize it.
2.  **Tasks:**
    *   Create a new ROS 2 package (e.g., `gripper_description`).
    *   Design a URDF file that describes a base link, two gripper fingers, and revolute joints to open/close them. Use `box` or `cylinder` geometries.
    *   Ensure your URDF file is placed in the `urdf` directory of your package.
    *   Configure your `CMakeLists.txt` and `package.xml` for the URDF.
    *   Create a launch file that starts `robot_state_publisher` with your URDF.
    *   Launch the URDF and visualize it in RViz.

**Exercise 4: Basic Python AI Integration (Pathfinding Hint)**

1.  **Objective:** Simulate a simple AI agent that reacts to a simulated "obstacle detected" signal.
2.  **Tasks:**
    *   Modify your `simple_publisher` to sometimes publish a special message (e.g., "Obstacle Detected!").
    *   Create a new Python AI agent node that subscribes to the `chatter` topic.
    *   If the agent detects "Obstacle Detected!", it should publish a `Twist` message with a specific angular velocity (e.g., turn left).
    *   Create a `dummy_controller` that subscribes to the `robot_command` topic and prints the received command.
    *   Run all three nodes and observe how the agent reacts to the "obstacle."

---

### Learning Objectives Review

Let's revisit the learning objectives to ensure you have a solid grasp of the module's content.

1.  **Understand ROS 2 architecture:**
    *   You should now understand that ROS 2 is a middleware framework composed of nodes, topics, and services for distributed robot control.
    *   You've learned about the publish-subscribe and service-client communication patterns.
    *   You've seen how packages organize ROS 2 code.

2.  **Master ROS 2 Nodes, Topics, and Services:**
    *   You've created custom Python nodes using `rclpy`.
    *   You've implemented publisher-subscriber patterns to send and receive messages asynchronously.
    *   You've implemented service-client patterns for synchronous request-response communication, including defining custom service types.

3.  **Learn to bridge Python Agents to ROS controllers using `rclpy`:**
    *   You've built a Python script that acts as an AI agent, subscribing to data, making simple decisions, and publishing commands.
    *   You've connected this agent to a dummy controller using ROS topics and messages (`geometry_msgs.msg.Twist`).

4.  **Understand URDF for humanoids:**
    *   You've learned the purpose of URDF for describing robot kinematics and structure.
    *   You've built and visualized a simple URDF model, understanding the concepts of links and joints.
    *   You understand how URDF is fundamental for simulating and controlling complex robots like humanoids.

---

**Congratulations!** You have completed Module 1. You have taken your first steps into the powerful world of ROS 2 and have a foundational understanding of its core concepts, communication mechanisms, and how to integrate Python code for robot control. In the next module, we will build upon this knowledge and explore more advanced ROS 2 features.

---
*Generated using Spec-Kit Plus & Gemini AI*
