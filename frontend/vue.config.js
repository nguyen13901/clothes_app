module.exports = {
  devServer: {
    headers: {
      "Access-Control-Allow-Origin": "https://gleaming-narwhal-31cfb9.netlify.app/",
    },
    host: "localhost",
    proxy: "https://gleaming-narwhal-31cfb9.netlify.app/",
    port: "8080",
  },
};
