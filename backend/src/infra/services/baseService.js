const Sequelize = require('sequelize');
const databaseService = require('./database');
const { checkError } = require('./database');

const { Op } = Sequelize;
class BaseService {
    constructor(schema, include = []) {
        this.schema = schema;
        this.include = include;
    }

    list = async (req, res) => {
        const payload = req.query;
        let skip = 0;
        let limit = 100;
        skip = parseInt(payload.skip, 10);
        delete payload.skip;
        limit = parseInt(payload.limit, 10);
        delete payload.limit;
        try {
            await this.schema.findAll({
                include: this.include,
                where: payload,
                offset: skip,
                limit,
                order: [
                    ['updated_at', 'DESC'],
                ],
            })
                .then((data) => {
                    res.status(200).json(data);
                })
                .catch((error) => {
                    const response = checkError(error);
                    const { statusCode } = response;
                    delete response.statusCode;
                    res.status(statusCode).json(response);
                });
        } catch (error) {
            console.log('Error list');
            console.log(error);
            const response = { success: false, detail: 'Error list' };
            res.status(400).json(response);
        }
    };

    create = async (req, res) => {
        
        try {
            const { body } = req;
            await this.schema.create(
                body,
            )
                .then((data) => {
                    const resSucces = data.dataValues;
                    res.status(201).json(resSucces);
                })
                .catch((error) => {
                    const response = checkError(error);
                    const { statusCode } = response;
                    delete response.statusCode;
                    res.status(statusCode).json(response);
                });
        } catch (error) {
            console.log('Error create');
            console.log(error);
            const response = { success: false, detail: 'Error create' };
            res.status(400).json(response);
        }
    };

    update = async (req, res) => {
        try {
            const { id } = req.params;
            const { body } = req;
            await this.schema.update(
                body,
                {
                    where: {
                        id,
                    },
                    returning: true,
                },
            )
                .then((data) => {
                    if (data[0] == 1) {
                        const response = data[1][0].dataValues;
                        res.status(201).json(response);
                    } else {
                        const response = { success: false, detail: 'Object not found' };
                        res.status(404).json(response);
                    }
                })
                .catch((error) => {
                    const response = checkError(error);
                    const { statusCode } = response;
                    delete response.statusCode;
                    res.status(statusCode).json(response);
                });
        } catch (error) {
            console.log('Error update');
            console.log(error);
            const response = { success: false, detail: 'Error update' };
            res.status(400).json(response);
        }
    };

    get = async (req, res) => {
        try {
            const { id } = req.params;
            await this.schema.findOne({
                include: this.include,
                where: { id },
            })
                .then((data) => {
                    if (data) {
                        res.status(200).json(data);
                    } else {
                        const response = { success: false, detail: 'Object not found' };
                        res.status(404).json(response);
                    }
                })
                .catch((error) => {
                    const response = checkError(error);
                    const { statusCode } = response;
                    delete response.statusCode;
                    res.status(statusCode).json(response);
                });
        } catch (error) {
            console.log('Error get');
            console.log(error);
            const response = { success: false, detail: 'Error get' };
            res.status(400).json(response);
        }
    };

    delete = async (req, res) => {
        try {
            const { id } = req.params;
            await this.schema.destroy({
                where: { id },
            })
                .then((data) => {
                    if (data) {
                        res.status(204).json({});
                    } else {
                        const response = { success: false, detail: 'Object not found' };
                        res.status(404).json(response);
                    }
                })
                .catch((error) => {
                    const response = checkError(error);
                    const { statusCode } = response;
                    delete response.statusCode;
                    res.status(statusCode).json(response);
                });
        } catch (error) {
            console.log('Error delete');
            console.log(error);
            const response = { success: false, detail: 'Error delete' };
            res.status(400).json(response);
        }
    };

    getFromCodes = async (id, payload) => {
        let response = {};
        let skip = 0;
        let limit = 100;
        if (payload.skip) {
            skip = parseInt(payload.skip, 10);
            delete payload.skip; // eslint-disable-line 
        }
        if (payload.limit) {
            limit = parseInt(payload.limit, 10);
            delete payload.limit; // eslint-disable-line 
        }
        try {
            await this.schema.findAndCountAll({
                include: this.include,
                distinct: true,
                where: {
                    id: { [Op.in]: id },
                    ...payload,
                },
                offset: skip,
                limit,
            })
                .then((data) => {
                    response.status = 200;
                    response.data = { total: data.count, data: data.rows };
                })
                .catch((error) => {
                    response = databaseService.checkError(error);
                    response.status = response.statusCode;
                    response.data = response.detail;
                });
        } catch (error) {
            console.log('Error list');
            console.log(error);
            response = { success: false, detail: 'Error list' };
        }
        return response;
    };

    getFromAttribute = async (payload, attribute, codes) => {
        let response = {};
        let skip = 0;
        let limit = 100;
        if (payload.skip) {
            skip = parseInt(payload.skip, 10);
            delete payload.skip; // eslint-disable-line 
        }
        if (payload.limit) {
            limit = parseInt(payload.limit, 10);
            delete payload.limit; // eslint-disable-line 
        }
        if (attribute) {
            payload[attribute] = { [Op.in]: codes }; // eslint-disable-line 
        }
        try {
            await this.schema.findAndCountAll({
                include: this.include,
                distinct: true,
                where: payload,
                offset: skip,
                limit,
            })
                .then((data) => {
                    response.status = 200;
                    response.data = { total: data.count, data: data.rows };
                })
                .catch((error) => {
                    response = databaseService.checkError(error);
                    response.status = response.statusCode;
                    response.data = response.detail;
                });
        } catch (error) {
            console.log('Error list');
            console.log(error);
            response = { success: false, detail: 'Error list' };
        }
        return response;
    };

    deleteWhere = async (attributes) => {
        let response = {};
        try {
            await this.schema.destroy({
                where: attributes,
            })
                .then((data) => {
                    if (data) {
                        response = {
                            data: true,
                            status: 201,
                        };
                    } else {
                        const detail = { success: false, detail: 'Object not found' };
                        response = {
                            data: detail,
                            status: 404,
                        };
                    }
                })
                .catch((error) => {
                    const responseError = checkError(error);
                    const { statusCode } = responseError;
                    delete responseError.statusCode;
                    response = {
                        data: responseError,
                        status: statusCode,
                    };
                });
        } catch (error) {
            console.log('Error delete');
            console.log(error);
            response = {
                data: { success: false, detail: 'Error creating boundaries' },
                status: 400,
            };
        }
        return response;
    };

    createMultiple = async (body) => {
        let response = {};
        try {
            await this.schema.bulkCreate(
                body,
                {
                    returning: true,
                },
            )
                .then(() => {
                    response = {
                        data: true,
                        status: 201,
                    };
                })
                .catch((error) => {
                    const responseError = checkError(error);
                    const { statusCode } = responseError;
                    delete responseError.statusCode;
                    response = {
                        data: responseError,
                        status: statusCode,
                    };
                });
        } catch (error) {
            console.log('Error create');
            console.log(error);
            response = {
                data: { success: false, detail: 'Error creating' },
                status: 400,
            };
        }
        return response;
    };
}
module.exports = BaseService;