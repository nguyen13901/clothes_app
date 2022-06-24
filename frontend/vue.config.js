module.exports = {
  devServer: {
    headers: {
      "Access-Control-Allow-Origin": "https://gleaming-narwhal-31cfb9.netlify.app",
    },
    host: "localhost",
    proxy: "http://localhost:8000/",
    port: "8080",
  },
};
