module.exports = {

    devServer: {
      proxy: {
        '/meta': {
          target: 'http://127.0.0.1:5000',
          changeOrigin: true,
          /*
          pathRewrite: {
            '^/api': '',
          },
          */
        },
      },
    },
  };
  
  