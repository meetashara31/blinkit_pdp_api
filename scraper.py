from utils import *
import jmespath

def extractor_details(data):
    product_name = extract_first([
        'response.snippets[0].data.itemList[0].tracking.widget_meta.child_widget_title',
        'response.snippets[2].data.title.text',
        'response.snippets[8].data.horizontal_item_list[0].tracking.click_map.name',
        'response.snippets[9].data.rfc_actions_v2.default[0].remove_from_cart.cart_item.display_name'
    ], data)

    price = extract_first([
        'response.snippets[9].data.stepper_data_v2.increment_actions.default[0].add_to_cart.cart_item.price',
        'response.snippets[9].tracking.impression_map.price',
        'response.snippets[2].tracking.common_attributes.price',
        'response.snippets[5].tracking.widget_meta.price'
    ], data)

    mrp = extract_first([
        'response.snippets[9].data.stepper_data_v2.increment_actions.default[0].add_to_cart.cart_item.mrp',
        'response.snippets[9].tracking.impression_map.mrp',
        'response.snippets[2].tracking.common_attributes.mrp',
        'response.snippets[5].tracking.widget_meta.mrp'
    ], data)

    product_type = extract_first([
        'response.snippets[2].tracking.common_attributes.ptype',
        'response.snippets[5].tracking.widget_meta.ptype'
    ], data)

    availability = extract_first([
        'response.snippets[2].tracking.common_attributes.state'
    ], data)

    merchant_id = extract_first([
        'response.snippets[5].tracking.widget_meta.merchant_id',
        'response.snippets[9].tracking.impression_map.merchant_id'
    ], data)

    product_id = extract_first([
        'response.snippets[2].data.identity.id',
        'response.snippets[2].tracking.common_attributes.product_id',
        'response.snippets[0].data.itemList[0].tracking.common_attributes.product_id',
        'response.snippets[0].tracking.common_attributes.product_id'
    ], data)

    unit = extract_first([
        'response.snippets[8].data.horizontal_item_list[0].data.title.text',
        'response.snippets[7].data.horizontal_item_list[0].data.title.text'
    ], data)

    # Extract images (could be list or str)
    images = extract_first([
        'response.snippets[0].data.itemList[0].data.click_action.show_gallery.assets[*].image_url',
        'response.snippets[0].data.itemList[1].data.click_action.show_gallery.assets[*].image_url'
    ], data)

    main_image = None
    other_images = []

    if isinstance(images, list) and images:
        main_image = images[0]
        other_images = images[1:]
    elif isinstance(images, str):
        main_image = images

    # Extract attributes
    attributes = jmespath.search(
        "response.tracking.le_meta.custom_data.seo.attributes[?type=='shown_to_customer']",
        data
    ) or []

    filtered_attributes = {}
    for attr in attributes:
        if 'attribute_name' in attr and 'value' in attr:
            key = attr['attribute_name'].strip()
            value = attr['value'].replace('\n', ' ').strip()
            if key not in filtered_attributes or (
                len(value) > len(filtered_attributes[key])
            ):
                filtered_attributes[key] = value

    return {
        'product_id': product_id,
        'product_name': product_name,
        'merchant_id': merchant_id,
        'mrp': mrp,
        'price': price,
        'type': product_type,
        'availability': availability,
        'unit': unit,
        'main_image': main_image,
        'images': other_images,   
        'others': filtered_attributes
    }
