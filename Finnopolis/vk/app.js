const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;
const VK_APP_ID = 'ID приложения';
const VK_SECRET_KEY = 'Защищённый ключ';

app.get('/login', (req, res) => {
  const redirectUri = `http://localhost:${port}/callback`;
  const vkAuthUrl = `https://oauth.vk.com/authorize?client_id=${VK_APP_ID}&redirect_uri=${redirectUri}&response_type=code&v=5.131`;

  res.send(`<a href="${vkAuthUrl}">Войти через ВКонтакте</a>`);
});

app.get('/callback', async (req, res) => {
  const code = req.query.code;
  const redirectUri = `http://localhost:${port}/callback`;
  const vkAccessTokenUrl = `https://oauth.vk.com/access_token?client_id=${VK_APP_ID}&client_secret=${VK_SECRET_KEY}&redirect_uri=${redirectUri}&code=${code}`;

  try {
    const response = await axios.get(vkAccessTokenUrl);
    const accessToken = response.data.access_token;
    const expiresIn = response.data.expires_in;
    res.send(`Токен авторизации VK: ${accessToken}, срок действия (в секундах): ${expiresIn}`);
  } catch (error) {
    console.error(error);
    res.status(500).send('Ошибка авторизации через ВКонтакте.');
  }
});

// Запуск сервера
app.listen(port, () => {
  console.log(`Сервер запущен на http://localhost:${port}`);
});
