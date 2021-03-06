from unittest import TestCase

from config import Config
from features import generate_features


class GenFeaturesTest(TestCase):
    # Testing the generate_features method
    # Note: 2020-06-11: These outputs were generated by running the test data through the actual function
    # It might be good to manually verify these outputs are desired
    def test_genfeatures_regulardata_1(self):
        # arrange
        test_data = [1.2, 0.05, -3.6, 18.9, -5.4, 8.004, 12.659, 0.143]
        test_config = Config(description='test')
        test_config.samplesize = 25
        test_config.fftfeatures = 0

        expected_output = [
            # "absolute" features:
            18.9, -5.4, 31.955999999999996, 3.9944999999999995, 0.6715, 6.2445, 4.5, 625.1072459999999, 5.008703664882724, 78.13840574999999,

            # "relative" features:
            62.182375500000006, 7.885580225956743, 6.894875, 5.1715, 5, 4, 0.0, 62.182375500000006, 327.383232918375, 8361.83212000199, 12.609, 1.9741094569925508, 0.6676601713176257, -0.8374466713399569, -0.5801193286061433, 11.739285714285714, 8.491135658762625, 6.894875, 3.8266270048666886, 3
        ]

        # act
        output = generate_features(test_data, test_config)

        # assert
        self.assertEqual(output, expected_output)

    def test_genfeatures_regulardata_2(self):
        # arrange
        test_data = [-0.97743333,  0.57411701, -1.18404237, -1.9459411 ,  2.09424604,
                     -1.51629388, -0.19929474, -0.41850196,  2.96623923, -0.4492357 ,
                      2.15653345,  0.43581939, -0.49928927,  1.40950917, -1.12943589,
                     -1.51951041,  0.46456604,  1.54215867,  1.49318207,  2.24503109,
                     -0.34385401,  1.85638915, -1.33505047,  2.58477635,  2.68607923]
        test_config = Config(description='test')
        test_config.samplesize = 25
        test_config.fftfeatures = 0

        expected_output = [
            # "absolute" features:
            2.96623923, -1.9459411, 10.99076376, 0.4396305504, 0.43581939, 1.3610612008, 1.40950917, 62.1417100629196, 1.7338234614687211, 2.485668402516784,

            # "relative" features:
            2.2923933816717774, 1.514065184089436, 1.343780871616, 1.42056976, 15, 15, 0.0, 2.2923933816717774, 0.4408139170486851, 8.521282447985339, 2.8338224800000003, 3.4439489765027846, 0.1270052221197356, -1.3784637240805915, -0.15458842356585242, 1.9175983399999998, 1.220088284173332, 1.343780871616, 0.6976004234163856, 16
        ]

        # act
        output = generate_features(test_data, test_config)

        # assert
        self.assertEqual(output, expected_output)

    def test_genfeatures_allzeros(self):
        # arrange
        test_data = [0, 0.0, 000, 0.0000, 0, 0.0, 0, 000.0]
        test_config = Config(description='test')
        test_config.samplesize = 25
        test_config.fftfeatures = 0

        expected_output = [
            # "absolute" features:
            0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0,

            # "relative" features:
            0.0, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0.0, -3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1
        ]

        # act
        output = generate_features(test_data, test_config)

        # assert
        self.assertEqual(output, expected_output)

    def test_genfeatures_allsamenum(self):
        # arrange
        test_data = [5.0, 5, 5.0, 5, 5.0000, 5, 5]
        test_config = Config(description='test')
        test_config.samplesize = 25
        test_config.fftfeatures = 0

        expected_output = [
            # "absolute" features:
            5.0, 5.0, 35.0, 5.0, 5.0, 5.0, 5.0, 175.0, 9.785580060704262, 25.0,

            # "relative" features:
            0.0, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, -3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1
        ]

        # act
        output = generate_features(test_data, test_config)

        # assert
        self.assertEqual(output, expected_output)

    def test_genfeatures_regulardata_1_withfftfeatures(self):
        # arrange
        test_data = [1.2, 0.05, -3.6, 18.9, -5.4, 8.004, 12.659, 0.143]
        test_config = Config(description='test')
        test_config.samplesize = 25
        test_config.fftfeatures = 1

        expected_output = [
            # "absolute" features:
            18.9, -5.4, 31.955999999999996, 3.9944999999999995, 0.6715, 6.2445, 4.5, 31.956000000000003, -1834.7090856955676, 9.600000000000009, 1.200000000000001, 623.667246, 625.1072459999999, 5.008703664882724, 78.13840574999999,

            # "relative" features:
            62.182375500000006, 7.885580225956743, 6.894875, 5.1715, 5, 4, 0.0, 62.182375500000006, 327.383232918375, 8361.83212000199, 12.609, 1.9741094569925508, 0.6676601713176257, -0.8374466713399569, -0.5801193286061433, 11.739285714285714, 8.491135658762625, 6.894875, 3.8266270048666886, 3
        ]

        # act
        output = generate_features(test_data, test_config)

        # assert
        self.assertEqual(output, expected_output)

    def test_genfeatures_regulardata_2_withfftfeatures(self):
        # arrange
        test_data = [-0.97743333,  0.57411701, -1.18404237, -1.9459411 ,  2.09424604,
                     -1.51629388, -0.19929474, -0.41850196,  2.96623923, -0.4492357 ,
                      2.15653345,  0.43581939, -0.49928927,  1.40950917, -1.12943589,
                     -1.51951041,  0.46456604,  1.54215867,  1.49318207,  2.24503109,
                     -0.34385401,  1.85638915, -1.33505047,  2.58477635,  2.68607923]
        test_config = Config(description='test')
        test_config.samplesize = 25
        test_config.fftfeatures = 1

        expected_output = [
            # "absolute" features:
            2.96623923, -1.9459411, 10.99076376, 0.4396305504, 0.43581939, 1.3610612008, 1.40950917, 10.990763759999998, -28.986804143372705, -24.435833250000005, -0.9774333300000001, 61.18633414832471, 62.1417100629196, 1.7338234614687211, 2.485668402516784,

            # "relative" features:
            2.2923933816717774, 1.514065184089436, 1.343780871616, 1.42056976, 15, 15, 0.0, 2.2923933816717774, 0.4408139170486851, 8.521282447985339, 2.8338224800000003, 3.4439489765027846, 0.1270052221197356, -1.3784637240805915, -0.15458842356585242, 1.9175983399999998, 1.220088284173332, 1.343780871616, 0.6976004234163856, 16
        ]

        # act
        output = generate_features(test_data, test_config)

        # assert
        self.assertEqual(output, expected_output)

    def test_genfeatures_regulardata_1_noabsolutefeatures(self):
        # arrange
        test_data = [1.2, 0.05, -3.6, 18.9, -5.4, 8.004, 12.659, 0.143]
        test_config = Config(description='test')
        test_config.samplesize = 25
        test_config.fftfeatures = 1  # turn on, but shouldn't show up in features due to absolute features disabled

        expected_output = [
            # "relative" features:
            62.182375500000006, 7.885580225956743, 6.894875, 5.1715, 5, 4, 0.0, 62.182375500000006, 327.383232918375, 8361.83212000199, 12.609, 1.9741094569925508, 0.6676601713176257, -0.8374466713399569, -0.5801193286061433, 11.739285714285714, 8.491135658762625, 6.894875, 3.8266270048666886, 3
        ]

        # act
        output = generate_features(test_data, test_config, include_absolute_features=False)

        # assert
        self.assertEqual(output, expected_output)

    def test_genfeatures_regulardata_2_noabsolutefeatures(self):
        # arrange
        test_data = [-0.97743333,  0.57411701, -1.18404237, -1.9459411 ,  2.09424604,
                     -1.51629388, -0.19929474, -0.41850196,  2.96623923, -0.4492357 ,
                      2.15653345,  0.43581939, -0.49928927,  1.40950917, -1.12943589,
                     -1.51951041,  0.46456604,  1.54215867,  1.49318207,  2.24503109,
                     -0.34385401,  1.85638915, -1.33505047,  2.58477635,  2.68607923]
        test_config = Config(description='test')
        test_config.samplesize = 25

        expected_output = [
            # "relative" features:
            2.2923933816717774, 1.514065184089436, 1.343780871616, 1.42056976, 15, 15, 0.0, 2.2923933816717774, 0.4408139170486851, 8.521282447985339, 2.8338224800000003, 3.4439489765027846, 0.1270052221197356, -1.3784637240805915, -0.15458842356585242, 1.9175983399999998, 1.220088284173332, 1.343780871616, 0.6976004234163856, 16
        ]

        # act
        output = generate_features(test_data, test_config, include_absolute_features=False)

        # assert
        self.assertEqual(output, expected_output)

    def test_genfeatures_allzeros_noabsolutefeatures(self):
        # arrange
        test_data = [0, 0.0, 000, 0.0000, 0, 0.0, 0, 000.0]
        test_config = Config(description='test')
        test_config.samplesize = 25

        expected_output = [
            # "relative" features:
            0.0, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0.0, -3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1
        ]

        # act
        output = generate_features(test_data, test_config, include_absolute_features=False)

        # assert
        self.assertEqual(output, expected_output)

    def test_genfeatures_allsamenum_noabsolutefeatures(self):
        # arrange
        test_data = [5.0, 5, 5.0, 5, 5.0000, 5, 5]
        test_config = Config(description='test')
        test_config.samplesize = 25

        expected_output = [
            # "relative" features:
            0.0, 0.0, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, -3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1
        ]

        # act
        output = generate_features(test_data, test_config, include_absolute_features=False)

        # assert
        self.assertEqual(output, expected_output)
