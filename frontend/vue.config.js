module.exports = {
  devServer: {
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    host: "localhost",
    proxy: "https://55cd-190-2-130-168.eu.ngrok.io/",
    port: "8080",
  },
};
