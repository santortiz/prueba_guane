const databaseService = {};

databaseService.checkError = (error) => {
    console.log(error);
    let resError = {};
    const errorName = error.name;
    switch (errorName) {
    case 'SequelizeUniqueConstraintError':
        resError = {
            success: false, detail: 'El objeto que intenta crear ya existe en la base de datos', key: error.errors[0].message, statusCode: 422,
        };
        return (resError);
    case 'SequelizeValidationError':
        resError = {
            success: false, detail: 'Los campos deben estar completos', key: error.errors[0].message, statusCode: 422,
        };
        return (resError);
    case 'SequelizeForeignKeyConstraintError':
        resError = {
            success: false, detail: 'Fallo en una clave foranea', key: error.index, statusCode: 422,
        };
        return (resError);
    case 'SequelizeDatabaseError':
        resError = {
            success: false, detail: 'Fallo en una columna', key: `${error.original}`, statusCode: 422,
        };
        return (resError);
    default:
        throw error;
    }
};

module.exports = databaseService;
