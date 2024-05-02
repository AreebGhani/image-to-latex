# Image to LaTeX Converter

This Flask application allows you to upload an image containing LaTeX equations and receive the corresponding LaTeX code as a response.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/AreebGhani/image-to-latex.git
   ```

2. Navigate to the project directory:

    ```bash
    cd image-to-latex
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask server:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to <http://localhost:5000>.
3. Upload an image containing LaTeX equations.
4. The server will respond with the LaTeX code extracted from the image.

## API Endpoints

POST /: Upload an image containing LaTeX equations.
Request Input Name: 'image'.

## License

This project is licensed under the MIT License - see the [License](LICENSE) file for details.
