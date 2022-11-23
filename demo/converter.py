import tensorflow as tf

converter = tf.compat.v1.lite.TFLiteConverter.from_saved_model(saved_model_dir='saved_model/')
converter.allow_custom_ops = True
converter.optimizations = {tf.lite.Optimize.DEFAULT}
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
converter._experimental_lower_tensor_list_ops = False
tflite_model = converter.convert()

# Save the model.
with open('re.tflite', 'wb') as f:
  f.write(tflite_model)
