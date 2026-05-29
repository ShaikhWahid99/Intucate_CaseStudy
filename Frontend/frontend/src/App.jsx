import { useState } from "react";
import "./App.css";

function App() {

  const [singleInput, setSingleInput] = useState("");
  const [singleResponse, setSingleResponse] = useState("");

  const [bulkInput, setBulkInput] = useState("");
  const [bulkResponses, setBulkResponses] = useState([]);

  const [loading, setLoading] = useState(false);

  // single chat
  const handleSingleChat = async () => {

    if (!singleInput.trim()) return;

    try {

      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            userInput: singleInput
          })
        }
      );

      const data = await response.json();

      setSingleResponse(data.response);

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };

  // bulk chat
  const handleBulkChat = async () => {

    const inputs = bulkInput
      .split("\n")
      .filter(input => input.trim());

    if (inputs.length === 0) return;

    try {

      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/bulk-chat",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            inputs
          })
        }
      );

      const data = await response.json();

      setBulkResponses(data.responses);

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };

  return (
    <div className="container">

      <h1>AI Chatbot</h1>

      {/* single chat */}

      <div className="card">

        <h2>Single Chat</h2>

        <input
          type="text"
          placeholder="Ask something..."
          value={singleInput}
          onChange={(e) =>
            setSingleInput(e.target.value)
          }
        />

        <button onClick={handleSingleChat}>
          Send
        </button>

        {
          loading && <p>Loading...</p>
        }

        {
          singleResponse && (
            <div className="response">
              {singleResponse}
            </div>
          )
        }

      </div>

      {/* bulk chat */}

      <div className="card">

        <h2>Bulk Chat</h2>

        <textarea
          rows="8"
          placeholder="One question per line"
          value={bulkInput}
          onChange={(e) =>
            setBulkInput(e.target.value)
          }
        />

        <button onClick={handleBulkChat}>
          Process Bulk
        </button>

        {
          bulkResponses.map((item, index) => (

            <div
              className="response"
              key={index}
            >
              {
                item.response || item.error
              }
            </div>
          ))
        }

      </div>

    </div>
  );
}

export default App;