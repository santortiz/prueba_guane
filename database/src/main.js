const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const settings = require('./config');
const routes = require('./api/index');
const sequelize = require('./database');
const app = express();

app.use(cors());
app.use(morgan(':method :url :status :res[content-length] - :response-time ms'));
app.use(express.json());
app.use(express.urlencoded({ extended: true}));
app.use(routes);

app.set('port', settings.PORT || 3000);

app.listen(app.get('port'), ()=>{
    console.log("Server on port " + app.get('port'))

    sequelize.authenticate().then(() => {
        console.log('Estas conectado a la BD');
    });

    sequelize.sync({force: settings.FORCE}).then(() => {
        console.log('tables created successfully!');
     }).catch((error) => {
        console.error('Unable to create table: ', error);
     });

    
});