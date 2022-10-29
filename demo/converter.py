import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir='tf_saved_model/')
converter.optimizations = {tf.lite.Optimize.DEFAULT}
tflte_model = converter.convert()
