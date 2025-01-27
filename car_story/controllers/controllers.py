from odoo import http
from odoo.http import request
import base64
import mimetypes

class CarStoryWebsite(http.Controller):

    @http.route(['/car/story'], type='http', auth='public', website=True)
    def car_story_form(self, **kwargs):
        # Fetch the selection options dynamically from the model
        CarStory = request.env['car.story']
        color_options = dict(CarStory._fields['color'].selection)
        make_options = dict(CarStory._fields['make'].selection)
        year_options = [str(year) for year in range(1990, 2026)]

        # Pass options to the template
        return request.render('car_story.car_story_template', {
            'color_options': color_options,
            'make_options': make_options,
            'year_options': year_options,
        })

    @http.route(['/car/story/submit'], type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def car_story_submit(self, **kwargs):
        image_ids = []
        for file in request.httprequest.files.getlist('image'):
            file_content = file.read()
            image_data = base64.b64encode(file_content).decode('utf-8')  # Decode bytes to str
            mime_type, _ = mimetypes.guess_type(file.filename)
            mime_type = mime_type.split('/')[1] if mime_type else 'png'
            attachment = request.env['ir.attachment'].sudo().create({
                'name': file.filename,
                'datas': image_data,
                'res_model': 'car.story',
                'res_id': 0,  # Will be updated after car_story creation
                'type': 'binary',
            })
            image_ids.append(attachment.id)
        car_story_data = {
            'owner_name': kwargs.get('owner_name'),
            'color': kwargs.get('color'),
            'make': kwargs.get('make'),
            'model': kwargs.get('model'),
            'vin': kwargs.get('vin'),
            'mileage': kwargs.get('mileage'),
            'year': kwargs.get('year'),
            'reached_company': kwargs.get('reached_company') == 'on',
            'out_of_pocket': kwargs.get('out_of_pocket'),
            'story': kwargs.get('story'),
            'image_ids': [(6, 0, image_ids)],
        }
        car_story = request.env['car.story'].sudo().create(car_story_data)
        for attachment in car_story.image_ids:
            attachment.write({'res_id': car_story.id})

        return request.redirect('/car/story/thankyou')

    @http.route(['/car/story/thankyou'], type='http', auth='public', website=True)
    def car_story_thank_you(self, **kwargs):
        return request.render('car_story.car_story_thank_you_template', {})

    @http.route('/get_story_product', auth="public", type='json')
    def get_story_product(self):
        stories = request.env['car.story'].sudo().search([], order='create_date desc', limit=6)
        story_count = request.env['car.story'].sudo().search_count([])
        return http.Response(template='car_story.new_story_dynamic', qcontext={'story_ids': stories,
                                                                               'story_count': story_count}).render()
    
    @http.route('/explore', type='http', auth='public', website=True)
    def explore_images(self, page=1, limit=20, **kwargs):
        all_image_records = request.env['car.story'].sudo().search([]).mapped('image_ids')
        return request.render('car_story.explore_template', {
            'all_image_records': all_image_records,
        })