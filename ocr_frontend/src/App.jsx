import axios from "axios";
import { useState } from "react";
import "./App.css";

const App = () => {
  const [ocrResult, setOcrResult] = useState("");
  const [selectedFile, setSelectedFile] = useState("");
  const [imageUrl, setImageUrl] = useState("")

  const handleSubmit = async (event) => {
    event.preventDefault();
    // console.log(event);
    // setOcrResult("event")
    const formData = new FormData();
    if (selectedFile) {
      formData.append("image", selectedFile);
    }

    try {
      const response = await axios.post(
        "http://localhost:8002/api/ocr/",
        formData,
        { headers: { "Content-Type": "multpart/form-data" } }
      );
      if (response.data) {
        setOcrResult(response.data.text);
      }
    } catch (error) {
      console.error("There was an error processing the image", error);
    }
  };

  const handleFileChange = (event) => {
    console.log(event.target.files);
    if (event.target.files) {
      console.log(URL.createObjectURL(event.target.files[0]));
      setImageUrl(URL.createObjectURL(event.target.files[0]))
      setSelectedFile(event.target.files[0]);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>OCR with Django using EasyOCR</h1>
        <form onSubmit={handleSubmit}>
          <input type="file" onChange={handleFileChange} />
          <button type="submit">Upload and Process</button>
        </form>

        {imageUrl && (
          <div style={{ width: "400px", height: "400px", margin: "0 auto"}}>
            <img src={imageUrl} alt="image" style={{ width: '100%', height: '100%', objectFit: 'contain' }} />
          </div>
        )}

        {ocrResult && (
          <div>
            <h2>OCR Result:</h2>
            <p>{ocrResult}</p>
          </div>
        )}
      </header>
    </div>
  );
};

export default App;
