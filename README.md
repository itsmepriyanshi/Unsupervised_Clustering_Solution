# Mall Customer Segmentation Model

## Overview
This project aims to segment mall customers into different groups using unsupervised clustering techniques. The goal is to help mall owners target the right audience for marketing different products effectively. The dataset contains hypothetical customer data, including attributes like CustomerID, Gender, Age, Annual Income, and Spending Score.
## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/mall_customer_segmentation.git
    cd mall_customer_segmentation
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Prepare the data:
    ```bash
    python src/data_preparation.py
    ```

2. Perform clustering:
    ```bash
    python src/clustering.py
    ```

3. Visualize the results:
    ```bash
    python src/visualization.py
    ```

4. Run the main script:
    ```bash
    python main.py
    ```
