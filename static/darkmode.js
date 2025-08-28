(function(){
  const key = "prefers-dark";
  const root = document.documentElement;
  function setDark(on){
    if (on) root.classList.add("dark"); else root.classList.remove("dark");
    localStorage.setItem(key, on ? "1":"0");
    document.getElementById("themeBtn").textContent = on ? "Light Mode" : "Dark Mode";
  }
  const saved = localStorage.getItem(key);
  setDark(saved === "1");
  document.getElementById("themeBtn").addEventListener("click", function(){
    const isDark = root.classList.contains("dark");
    setDark(!isDark);
  });
})();
