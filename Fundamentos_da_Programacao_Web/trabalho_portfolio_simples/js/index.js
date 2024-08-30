function handleSections() {
  const internalLinks = document.querySelectorAll("a[href^='#']");
  const jsSections = document.querySelectorAll(".js-section");
  const hambMenu = document.querySelector("#hambMenuBtn");
  const className = "visible";

  if (internalLinks.length && jsSections.length) {
    // primeira parte
    jsSections[0].classList.add(className);

    function showSection(href) {
      const section = document.querySelector(href);
      jsSections.forEach(item => {
        item.classList.remove(className);
      })
      section.classList.add(className);
    }

    // segunda parte
    internalLinks.forEach((link) => {
      link.addEventListener("click", (e) => {
        e.preventDefault();
        const href = link.getAttribute("href");
        showSection(href);
      })
    })

    // terceira parte
    function handleHambMenu() {
      const tabNav = document.querySelector(".tabNav");
      tabNav.classList.toggle("visible");
    }
    hambMenu.addEventListener("click", handleHambMenu);

    // Ao chamar a função "handleSection", com uma condicional, primeiro verificamos a integridade dos links internos (internalLinks) e também das seções (jsSections)
    // Antes de prosseguir, adicionamos a classe "visible" na primeira seção (índice zero), para garantir que ela começará visível
    // A função "showSection" recebe um parâmetro "href", depois percorre todas as seções com um loop e remove de todas elas a classe "visible"
    // Em seguida, dentre as 4 seções, acessa uma delas por meio do "href" recebido como parâmetro, adicionando a a classe "visible" (a segunda parte da função é quem envia o href)

    // A segunda parte da função percorre os links internos, obtendo cada um deles (link)
    // Depois, adicionamos um escutador em cada link, atribuindo-lhes uma ação de click, prevenindo inclusive o comportamento padrão
    // Por último (e o mais importante) chamamos a função "showSection", passando para ela o href do link interno atual (que foi clicado)
    // Então, quando a função "showSection" receber o href do link interno, realizaremos com ele um "querySelector" por ID e, assim, saberemos qual seção (section) queremos mostrar
    // Dessa forma, saberemos exatamente em qual seção queremos adicionar a classe "visible"
    
    // A terceira parte adiciona um escutador no ícone de menu hambúrguer, visível apenas em telas de tamanho igual ou inferior a 768px, o qual controlará a adição ou exclusão da classe "visible", que é responsável por mostrar ou não o menu mobile
  }
}


handleSections();