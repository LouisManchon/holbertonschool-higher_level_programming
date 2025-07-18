fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const list = document.querySelector('#list_movies');
    data.results.forEach(film => {
        const listItem = document.createElement('li');
        listItem.textContent = film.title;
        list.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Erreur lors de la récupération:', error);
  });
