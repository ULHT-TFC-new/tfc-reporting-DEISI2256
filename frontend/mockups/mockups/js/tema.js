// Alterna entre o tema claro e o escuro mudando só o atributo data-tema.
(function () {
  var raiz = document.documentElement;
  try { var guardado = localStorage.getItem("tema"); if (guardado) raiz.setAttribute("data-tema", guardado); } catch (e) {}
  document.addEventListener("DOMContentLoaded", function () {
    var botao = document.getElementById("mudar-tema");
    if (!botao) return;
    function atualizar() {
      var escuro = raiz.getAttribute("data-tema") === "escuro";
      botao.textContent = escuro ? "Modo claro" : "Modo escuro";
      botao.setAttribute("aria-pressed", escuro ? "true" : "false");
    }
    botao.addEventListener("click", function () {
      var novo = raiz.getAttribute("data-tema") === "escuro" ? "claro" : "escuro";
      raiz.setAttribute("data-tema", novo);
      try { localStorage.setItem("tema", novo); } catch (e) {}
      atualizar();
    });
    atualizar();
  });
})();
