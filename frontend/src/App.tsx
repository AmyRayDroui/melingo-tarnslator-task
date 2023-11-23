import React, { useEffect, useState } from "react";
import { BASE_API_URL } from "./ustils/constants";
import DOMPurify from "dompurify";

type ServerResults = {
  message?: string;
  originalWord?: string;
  translation?: String;
  examples?: string[];
};

function App() {
  const [inputValue, setInputValue] = useState("");
  const [error, setError] = useState("");

  const [serverResult, setServerResult] = useState<ServerResults>({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch(
          `${BASE_API_URL}/translate?word=${inputValue.toLowerCase()}`
        );
        const data = await res.json();
        console.log(data);
        setServerResult(data);
      } catch (error) {
        console.error("Error:", error);
      }
    };
    fetchData();
  }, [inputValue]);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.value.includes(" ")) {
      setError("Please enter a word and not a sentence");
    } else {
      setError("");
    }
    setInputValue(event.target.value);
  };

  return (
    <div className="h-screen flex flex-col justify-center align-middle bg-gradient-to-tl from-lilac to-blueNavy text-light">
      <main className=" min-h-max mx-auto p-6 rounded-3xl bg-containerBg">
        <header className="mb-6">
          <h1 className="text-xl md:text-5xl font-bold">
            Welcome to Melingo's Translator
          </h1>
          <h2 className="text-lg mt-1 ml-2">please type in a word</h2>
        </header>

        <input
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Type something..."
          className=" bg-containerBg text-lg py-2 px-3 rounded-md text-gray-900 focus:outline-none"
        />
        <p className="text-red text-sm">{error}</p>
        <div className="ml-1 mt-4 text-md md:text-lg">
          {!Object.keys(serverResult).length ? null : serverResult.message ? (
            <p>{serverResult.message}</p>
          ) : (
            <>
              <h3 className="font-semibold">
                Translation:{" "}
                <strong className="italic">{serverResult.translation}</strong>
              </h3>
              {serverResult.examples && (
                <div>
                  <h3 className="font-semibold">Examples:</h3>
                  <ul className="list-disc ml-10 ">
                    {serverResult.examples.map((example) => (
                      <li
                        dangerouslySetInnerHTML={{
                          __html: DOMPurify.sanitize(example),
                        }}
                      ></li>
                    ))}
                  </ul>
                </div>
              )}
            </>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
