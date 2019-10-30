module.exports = {
    assetsDir: 'static', // For simple configuration of static files in Flask (the "static_folder='template/dist/static'" part in application.py)
    devServer: {
        proxy: 'http://localhost:5000' // So that the client dev server can access your Flask routes
    }
};
