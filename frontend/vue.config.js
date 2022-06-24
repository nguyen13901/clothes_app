module.exports = {
  devServer: {
    headers: {
      "Access-Control-Allow-Origin": "http://localhost:8000/",
    },
    host: "localhost",
    proxy: "http://localhost:8000/",
    port: "8080",
  },
};
