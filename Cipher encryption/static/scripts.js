function encryptText() {
    const text = document.getElementById("inputText").value;
    const shift = document.getElementById("shiftValue").value;
  
    fetch("/encrypt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text, shift: shift }),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("outputText").value = data.result;
      });
  }
  
  function decryptText() {
    const text = document.getElementById("inputText").value;
    const shift = document.getElementById("shiftValue").value;
  
    fetch("/decrypt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text, shift: shift }),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("outputText").value = data.result;
      });
  }
  
  function clearText() {
    document.getElementById("inputText").value = "";
    document.getElementById("outputText").value = "";
    document.getElementById("shiftValue").value = 0;
  }
  