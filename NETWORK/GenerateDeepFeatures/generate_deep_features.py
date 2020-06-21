import graphlab

deep_learning_model = graphlab.load_model('../DeepLearningModel/model.conf')
image_data_without_deepfeatures = graphlab.SFrame('../Dataset_SFrame/image_data_without_deepfeatures')
#image_data_without_deepfeatures['deep_features'] = deep_learning_model.extract_features(image_data_without_deepfeatures)
#image_data_without_deepfeatures.save('../Dataset_SFrame/image_data_with_deepfeatures')
sample_data = image_data_without_deepfeatures[200:]
sample_data['deep_features'] = deep_learning_model.extract_features(sample_data)
print sample_data
sample_data.save('../Dataset_SFrame/image_data_with_deepfeatures/df' + '-3')