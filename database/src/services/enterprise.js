const Enterprise = require('../infra/models/enterprise');
const BaseService = require('../infra/services/baseService');
const { checkError } = require('../infra/services/database');

class EnterpriseService extends BaseService {

    list = async (payload) => {
        let response = {};
        const filter = payload;
        let skip= 0;
        let limit= 100;
        skip= parseInt(filter.skip, 10);
        delete filter.skip; // ¿Por qué se eliminan?
        limit = parseInt(filter.limit, 10);
        delete filter.limit;

        try {
            await this.schema.findAll({
                include: this.include,
                offset: skip,
                limit,
                order: [
                    ['id', 'DESC']
                ],
            }).then((data) => {
                response= {
                    data,
                    status: 200,
                }
            })
            .catch((error) => {
                response = {
                    data: checkError(error),
                    status: 400,
                };
            });

        } catch (error) {
            console.log('Error list');
            console.log(error);
            response = {
                data: { success: false, detail: 'Error listing' },
                status: 400,
            };
        }
        return response;
    }

    //hereda el resto del crud desde el baseService


}

const service = new EnterpriseService(Enterprise);
module.exports = service;



