from unittest import TestCase

import numpy as np

from kmeans import KMeans


class KMeansTest(TestCase):
    # Testing the KMeans model

    def setUp(self) -> None:
        # Add large data set for testing with multiple tests:
        self.large_test_data = [
            np.array([21.10706321, 0.89717412, -1.57582408, 3.9582668, 0.14747661, -4.48933337]),
            np.array([19.13134769, -0.58915519, -2.56546829, 1.30749792, 0.61336781, -6.28298825]),
            np.array([-0.7391333, 18.63626707, 4.53578063, -27.46303431, 18.90265296, 6.80772898]),
            np.array([9.58283058, -6.22541085, 7.54521367, 6.33606351, 21.52410707, -11.32621921]),
            np.array([1.27591237, 22.94224985, 8.70601716, -13.35082301, 11.14466448, 18.02100869]),
            np.array([-97.96817231, 30.55689993, -10.37621172, -6.62538191, 14.11358142, 33.089026]),
            np.array([14.44517829, -2.49141519, 6.82221436, 4.22357151, 18.99702448, -10.69324029]),
            np.array([-0.25815216, 21.57715657, 8.18403436, -25.01926721, 22.60070272, 12.44123602]),
            np.array([5.11535026, 25.32548622, 8.6770624, -21.79142271, 23.5773142, 16.38460599]),
            np.array([-99.33103388, 34.22313726, -11.68695324, -6.44524701, 12.18162016, 31.23623217]),
            np.array([-6.07366423, 30.37781652, -1.42335354, -22.06038331, 13.67147648, 15.75917865]),
            np.array([21.07913372, -4.15176988, -0.91713127, -0.11722332, 1.08393971, -6.60183239]),
            np.array([6.87430116, 24.14376564, -0.34479716, -27.58737551, 13.45233652, 15.98144052]),
            np.array([-97.6965527, 32.5786865, -8.80431335, -10.07714051, 13.59741812, 29.76919482]),
            np.array([-100.45890218, 32.18027042, -10.22342898, -7.65168191, 13.12824112, 32.52889796]),
            np.array([10.47479135, 28.10046427, 5.95510686, -24.05401781, 28.46584862, 9.80778437]),
            np.array([-100.53179015, 32.03190664, -13.73133765, -3.99449741, 11.77283836, 34.26429207]),
            np.array([-8.57858704, 21.18194155, 2.1362899, -17.24081521, 9.49242092, 29.16598507]),
            np.array([-99.70437575, 31.04472841, -11.77351583, -5.11393251, 12.19523187, 32.72821349]),
            np.array([-100.51579964, 33.32544936, -11.64227084, -2.85170631, 14.22935699, 30.30299834]),
            np.array([21.90668721, -0.47540222, 0.59251509, 3.34240102, -2.89954421, -4.18362582]),
            np.array([14.79122775, -2.45688429, 9.69503519, 9.40584541, 21.90325627, -14.8982019]),
            np.array([12.22841415, -1.72295536, 6.38472667, 6.29022091, 18.75724279, -12.44934697]),
            np.array([8.83981074, -5.64685436, 8.99223117, 5.44874841, 24.89194194, -15.6958913]),
            np.array([3.74699382, 27.9370456, -1.11275584, -33.93636391, 17.49686398, 6.46623736]),
            np.array([14.2877265, -0.53714412, 9.09453989, 9.93737261, 22.88502842, -10.60616444]),
            np.array([11.32173727, -0.15314665, 8.46842753, 5.59786201, 22.69936036, -14.32887403]),
            np.array([9.27516533, -3.08903427, 4.19769679, 8.15987481, 18.54249707, -13.84158597]),
            np.array([14.42486328, -2.63126352, 6.35947952, 6.34812101, 25.25379024, -13.59669036]),
            np.array([-0.96852827, 24.45047625, 11.30173875, -29.66326411, 23.16574869, 16.39431745]),
            np.array([12.87012989, -1.64032594, 10.65312006, 12.25806981, 21.45970117, -14.59657219]),
            np.array([-100.04054234, 33.99715044, -11.24457589, -5.35627561, 12.51465012, 33.95692137]),
            np.array([15.68629133, -3.90850247, 5.62490643, 10.08119431, 24.06059239, -10.52457157]),
            np.array([10.12922645, -4.91440736, 5.58624775, 10.19356891, 21.79713489, -13.71916381]),
            np.array([9.7191109, -1.91108787, 5.84165876, 8.61169231, 19.24792275, -12.81596531]),
            np.array([10.60837887, -2.28880031, 3.04171271, 8.14665581, 23.20815883, -13.2481882]),
            np.array([9.35666708, -3.97518208, 6.13155071, 1.9086331, 23.41746793, -14.15916027]),
            np.array([11.52706668, -1.7519055, 11.99098618, 10.68208501, 24.68981456, -14.98175711]),
            np.array([-3.72481474, 28.97846194, 13.88791408, -21.93960201, 18.65587323, 14.70184769]),
            np.array([24.04846565, -0.28322693, -4.5843195, -1.24432662, 2.08318691, -5.6588672]),
            np.array([23.17146623, -2.40514874, 0.03639663, 3.29884168, 0.17542281, -4.94759349]),
            np.array([12.62998018, -3.71465913, 9.05930997, 9.00163641, 21.8052661, -7.0208212]),
            np.array([9.19688856, -8.34994471, 8.25596531, 7.98725511, 23.19323166, -13.88493185]),
            np.array([-2.42852989, 20.62085812, -0.05401749, -19.05692141, 17.80181698, 11.26515178]),
            np.array([-99.33630704, 29.56031783, -12.55031342, -1.27997201, 13.07616692, 27.65149606]),
            np.array([4.87219243, 27.70885161, 8.32629116, -16.22143801, 16.19969057, 10.89951789]),
            np.array([-6.23244635, 34.40956281, 3.31247936, -24.47669371, 12.78271388, 18.55496296]),
            np.array([6.90992926, 26.35364452, 5.0526023, -23.02790121, 20.12537334, 24.3350042]),
            np.array([-4.783924, 27.5032625, 1.57113603, -29.28643901, 26.71650745, 14.90521716]),
            np.array([12.96375434, -3.84312899, 8.05609414, 3.5447241, 18.62504675, -14.58954751]),
            np.array([12.16605562, -0.67464799, 8.97603952, 7.86067601, 21.46011996, -17.36994499]),
            np.array([10.19441446, -4.99098327, 8.27506887, 8.16238851, 23.56912262, -10.1419887]),
            np.array([11.90522733, -6.35143161, 8.67491719, 9.24940571, 26.67490094, -13.77098102]),
            np.array([0.91626722, 36.88650559, 6.2137162, -13.16386281, 18.39761114, 8.06872332]),
            np.array([10.44095301, -3.07075791, 4.02704293, 8.836351, 22.61644143, -11.97749669]),
            np.array([-100.46339212, 33.15788973, -9.14272811, -7.10987091, 13.22316623, 31.57854124]),
            np.array([11.26121105, 1.16119766, 6.09455064, 8.18162791, 21.21957844, -15.71665486]),
            np.array([25.07856781, -2.0351461, 0.83632925, 6.00732337, -0.72603571, -7.2143272]),
            np.array([-2.78157471, 28.99547295, 4.11930563, -16.58555191, 13.82326688, 12.72738433]),
            np.array([13.16803222, -5.25450243, 7.05636003, 9.65513051, 20.42649126, -10.71958984]),
            np.array([-100.4204234, 36.71056463, -9.67715042, -4.73666661, 13.13144861, 29.09463599]),
            np.array([10.88608137, -0.37237482, 3.97074014, 5.7339871, 22.9053954, -14.94743794]),
            np.array([14.03738205, -3.18383629, 3.90230778, 9.38552979, 24.56526581, -9.98211231]),
            np.array([11.04258453, -5.45578124, 7.703507, 3.61050091, 22.87495125, -14.32515728]),
            np.array([-102.40054441, 27.96089705, -11.49896056, -4.23757071, 13.43312149, 31.43596635]),
            np.array([0.81214439, 27.5902556, 4.11841731, -24.58326271, 17.17395128, 12.17904444]),
            np.array([17.74491728, -1.90422928, -2.19038669, 4.63680198, -0.5189471, -4.29716746]),
            np.array([11.76449531, -6.82823554, 6.23697994, 8.0952186, 22.80515621, -8.67073274]),
            np.array([0.69620137, 25.13393002, 3.23300132, -25.09482641, 19.50094717, 13.19498677]),
            np.array([3.08891533, 23.54808525, 6.35195349, -24.31080821, 18.66932387, 4.84828781]),
            np.array([4.65608015, 26.62629563, 7.20379761, -13.16138001, 15.31622844, 10.31230469]),
            np.array([11.16702816, -4.76082429, 9.08492693, 4.93367461, 24.29611108, -13.26556437]),
            np.array([9.48021372, -1.73175473, 8.35552788, 7.36643171, 20.48373491, -10.88992766]),
            np.array([12.90442665, -3.37617232, 9.21381466, 12.60296121, 23.17031296, -19.22250735]),
            np.array([-99.98893956, 31.39587613, -12.94107312, -5.51126631, 11.54429295, 31.47941732]),
            np.array([9.79903953, -4.06113977, 10.02228045, 6.35481941, 24.48004944, -14.8527634]),
            np.array([26.87668872, 3.81697902, 1.19476677, 2.58123031, -2.07958381, -6.88248529]),
            np.array([-102.74976892, 32.2059693, -12.51670305, -6.81309101, 15.11092986, 32.58926791]),
            np.array([12.7332637, -3.95129991, 7.2325048, 9.20824691, 23.158806, -11.43393501]),
            np.array([0.60643982, 27.53614056, 4.57497003, -25.26574861, 23.83757958, 14.69135092]),
            np.array([-8.95674837, 27.90706983, -6.46024587, -25.71926851, 23.76301148, 20.17463649]),
            np.array([20.50043774, 0.94822615, 0.5533237, 4.26241218, -0.96544871, -4.45453172]),
            np.array([-101.60748956, 28.41831177, -11.96673914, -4.20630921, 15.37607117, 30.98808819]),
            np.array([10.89127013, -5.46957192, 9.2792432, 6.36448261, 22.90127795, -15.32138826]),
            np.array([-0.98335844, 24.76820514, -2.12465763, -19.42072041, 22.07650766, 4.86466705]),
            np.array([10.51748644, -3.01443123, 9.52926497, 4.2886911, 24.05270969, -12.07679931]),
            np.array([11.81473975, -8.73530929, 7.6040745, 8.18252951, 25.12133317, -10.10811642]),
            np.array([5.80193214, 25.74004505, 3.94289896, -23.94926851, 22.6128355, 5.84682139]),
            np.array([11.84917532, -4.57143453, 6.66570301, 10.66386281, 23.89742178, -11.00964116]),
            np.array([22.00236349, 0.23172983, 1.06962032, 3.05239414, -3.46106491, -4.05611776]),
            np.array([-102.2790488, 32.74863369, -10.79483798, -3.3217251, 14.37601058, 26.88597056]),
            np.array([21.83041511, 2.3261121, 0.35817789, 1.57001174, -3.64664931, -1.56282195]),
            np.array([-97.94163238, 33.29073005, -8.19499869, -7.05238651, 12.50097766, 27.49264327]),
            np.array([-97.40719184, 32.24494408, -11.87559361, -3.18336231, 15.64739762, 31.74710565]),
            np.array([7.28862466, 22.83745564, 2.2907722, -16.71906391, 6.91895071, 16.21307061]),
            np.array([16.2274722, -6.28999412, 6.08798632, 4.79273031, 24.06294109, -10.90764908]),
            np.array([-3.4906854, 29.36756284, 8.43634725, -20.62237901, 19.6086946, 5.43325227]),
            np.array([23.90429757, -2.90513541, -2.95403191, 2.21501781, -0.62954551, -6.57752756]),
            np.array([20.74731693, 4.19101825, 3.85646757, 1.49372586, -3.67917101, -0.5084429]),
            np.array([25.05552299, 2.08778293, 1.78893426, 4.50710436, -0.63000561, -7.26637601]),
            np.array([2.22028895e+01, 1.50870601e-03, 2.06416362e-01, 6.85990830e-01, -4.27340775e+00, -5.69427331e+00]),
            np.array([11.65555969, -5.62008584, 5.76085597, 9.86688171, 24.00215185, -12.0276699]),
            np.array([22.60754868, -1.70427623, 1.18546565, 1.27471122, -0.76951071, 0.3512687]),
            np.array([13.0595546, -7.74165081, 6.59599525, 7.07794881, 24.49887991, -14.50917842]),
            np.array([11.32021905, 3.12424776, 6.77473209, 6.23641867, 24.21102071, -9.79816668]),
            np.array([-103.62630624, 31.2106011, -9.21296974, -3.65320681, 12.18449901, 32.67934072]),
            np.array([14.34581771, -0.22760829, 7.39367197, 7.31286033, 22.15028991, -9.34696038]),
            np.array([12.09115799, -4.49774185, 6.68399375, 7.92259351, 26.31175467, -14.25190683]),
            np.array([9.77097153, -4.30241363, 8.32805292, 8.45857041, 23.66388227, -16.09597404]),
            np.array([7.19992, 24.16050308, 4.15352632, -17.33279621, 20.82322554, 18.96954227]),
            np.array([22.95645773, -3.92327063, -5.04429068, 1.99105121, 2.69096671, -4.99082452]),
            np.array([7.53817205, -2.43470067, 6.9229302, 4.78895451, 24.32803412, -13.08311206]),
            np.array([-100.14100363, 29.21773476, -10.16427558, -6.61946321, 13.69876276, 30.25240453]),
            np.array([12.65851479, -2.37530244, 8.51441125, 6.60028351, 20.3723611, -10.19780659]),
            np.array([-100.61116025, 29.67381834, -5.83303333, -7.65630081, 14.31976223, 33.87798523]),
            np.array([-101.26946435, 33.83504687, -12.68938814, -6.64812431, 14.59139453, 35.13764139]),
            np.array([-98.12177683, 30.59112827, -13.12709991, -4.61971471, 13.51350983, 30.33489746]),
            np.array([14.96658599, -2.70833338, 6.69737202, 10.94126541, 22.61876055, -10.09454678]),
            np.array([3.40523072, 24.71415658, 0.74973982, -23.48930031, 18.99185813, 4.13291272]),
            np.array([10.64397519, -1.18693242, 10.89723477, 8.64392331, 24.44134154, -13.88386822]),
            np.array([22.50964274, 1.74532169, -3.14016342, 2.46047961, -0.67365191, -6.70683591]),
            np.array([-100.67181567, 34.61326589, -9.3094382, -6.68309651, 13.45344976, 28.74790549]),
            np.array([-3.42517435, 19.51271214, 4.38513757, -11.9540451, 22.98184477, 14.08076583]),
            np.array([12.46241246, 1.21157001, 7.63297319, 5.20261681, 20.44461038, -16.71885874]),
            np.array([23.37148052, -1.5045749, 1.26938845, 3.77855369, 0.76836831, -2.89121535]),
            np.array([12.51488665, -4.25742423, 7.0746933, 9.95051571, 25.84235962, -11.29549792]),
            np.array([10.20009289, -3.37139562, 6.70000706, 6.99755191, 24.27270968, -12.69449405]),
            np.array([13.16138635, -6.9537596, 6.82291661, 7.28643601, 23.79427189, -11.62013555]),
            np.array([1.23799039, 23.94581606, 10.48706264, -22.78552171, 18.3362553, 21.20688569]),
            np.array([-99.14518136, 31.616054, -11.22857764, -3.99907031, 12.7405945, 33.74823742]),
            np.array([15.26500505, -1.23744825, 6.24559888, 9.50056591, 24.48195238, -12.74683642]),
            np.array([21.18172929, -1.40592946, -2.94016114, 2.71849244, -1.84674221, -4.33877929]),
            np.array([22.34845586, 1.53561838, 0.83284476, 1.84395525, -1.09253001, -7.79978413]),
            np.array([10.78122932, -2.48544103, 6.00473006, 9.24721331, 21.30789969, -10.78148754]),
            np.array([10.81978637, -4.47720248, 10.05783395, 6.50526211, 23.28292167, -12.60120313]),
            np.array([-97.41747203, 34.23234279, -7.37029018, -3.23700321, 13.50805506, 29.84104807]),
            np.array([-5.98175244, 29.15728914, 7.76600183, -23.05203471, 22.129445, 6.0192587]),
            np.array([-1.7108951, 30.07013313, 13.04505557, -16.85686761, 29.14916213, 12.4309042]),
            np.array([24.95972652, -0.93737298, -0.19993163, 1.90750616, -0.78163591, -7.70422425]),
            np.array([18.73756338, -1.17863844, -0.67019581, 2.64812316, 0.15184081, -3.79278048]),
            np.array([13.32406551, -2.15660867, 7.61644333, 5.9812611, 22.12566955, -15.11894766]),
            np.array([14.75218644, -0.14243997, 5.33322531, 6.53692501, 21.17711242, -14.24113627]),
            np.array([-2.60426958, 16.19265125, 4.11378629, -20.48508451, 23.45455152, 11.43877617]),
            np.array([1.21640796, 31.49954742, 8.54092125, -20.11584821, 23.53705389, 15.73367508]),
            np.array([-6.34001158, 23.81341612, 7.21427803, -25.73585731, 19.52801816, 13.92583949]),
            np.array([4.24693454, 28.87991728, 6.01399275, -22.84923581, 21.24423563, 20.68010605]),
            np.array([17.6724926, -0.91891335, 1.14306087, 2.98750245, 2.60860651, -5.70406869]),
            np.array([12.23795638, -3.31634563, 5.45137699, 8.1281791, 21.88151668, -11.34583121]),
            np.array([13.2456984, -4.6136567, 5.49532526, 6.78085629, 24.17816351, -9.62911962]),
            np.array([-98.50892545, 30.15574371, -7.07786928, -5.08085121, 13.38061297, 27.1388406]),
            np.array([12.84050196, -1.44002075, 7.57276384, 5.76427351, 22.74446546, -14.09880187]),
            np.array([12.46872682, -4.54646443, 2.96997254, 9.10286611, 24.49718883, -11.26823271]),
            np.array([4.76080877, 24.51959648, 1.9113715, -25.12415381, 17.89766435, 2.54262077]),
            np.array([-1.55011036, 21.66698027, 10.54439327, -21.74505751, 13.31351411, 20.12828393]),
            np.array([-102.32527697, 30.75948385, -13.36348965, -2.50401701, 8.38991706, 27.47078137]),
            np.array([-96.22436017, 32.36377499, -10.68236596, -3.34833261, 10.16750767, 29.01773684]),
            np.array([22.98986004, -2.29901631, 0.22861471, 3.09963604, -0.2618641, -6.39164396]),
            np.array([20.84568904, 2.73892919, 3.38891006, 4.51122563, -1.03265051, -7.85677246]),
            np.array([7.28496673, 32.21001601, 4.93336558, -18.6155961, 23.14676597, 10.70059123]),
            np.array([25.72346677, 1.24622481, 3.1090947, 5.80855693, 0.73728151, -6.58222945]),
            np.array([-100.54212931, 32.79912313, -15.33714301, -5.91174491, 12.01316052, 30.64156916]),
            np.array([23.86220817, -0.56964045, -0.50331047, 2.43350868, -2.96160821, -1.78097209]),
            np.array([22.30040549, -0.44730244, -2.16910549, 2.84461292, -2.6116291, -9.27911287]),
            np.array([-0.49415964, 19.70018205, 1.92046162, -19.99140821, 21.3987219, 11.52702092]),
            np.array([-3.79753493, 21.28137532, 7.84538085, -19.86294361, 15.76390233, 9.66014702]),
            np.array([-3.43226471, 20.44299262, 6.7475745, -19.74828271, 16.79115303, 16.80050674]),
            np.array([-11.17965514, 27.13883882, -4.14328083, -21.49735511, 33.9474291, 15.55717216]),
            np.array([10.79258313, -3.65234213, 12.23125197, 5.4055461, 22.36063805, -12.90129239]),
            np.array([11.44094712, -1.67975308, 8.5162656, 6.14157801, 20.02374043, -15.40890283]),
            np.array([-103.96934877, 33.75555369, -8.73156528, -4.84514591, 14.59273238, 29.50907891]),
            np.array([10.32424947, -5.30484699, 9.07740146, 8.44932801, 27.08119462, -11.86029064]),
            np.array([-1.34096381, 26.16619896, -6.11011125, -22.53582781, 16.61745798, 9.39392897]),
            np.array([-101.58218891, 32.42548976, -11.14818742, -7.14591581, 13.30203595, 31.57994747]),
            np.array([1.85253926e+01, -2.31724911e+00, -9.26075072e-01, 2.72810839e+01, 1.61513675e-02, -5.87446442e+00]),
            np.array([-100.19381903, 32.27462169, -9.90617801, -6.44252851, 11.34503716, 28.11570878]),
            np.array([-100.96892646, 31.5964783, -6.37747763, -3.79783491, 12.15733624, 29.72150747]),
            np.array([23.60474405, -0.34108803, 2.0862284, 4.76981596, -1.64518981, -4.14729186]),
            np.array([2.93692176, 22.39384666, 1.37348217, -20.39867121, 19.5178764, 15.18884587]),
            np.array([11.8456806, -1.94790248, 11.39417358, 6.87428931, 21.70498084, -14.57068721]),
            np.array([12.36634187, -5.02667079, 7.95611593, 7.95459621, 23.2121465, -14.34524974]),
            np.array([13.51277981, -1.77559512, 8.52388482, 8.4450351, 21.98081507, -14.6371471]),
            np.array([-96.61954388, 32.40327738, -12.71953749, -3.05391111, 13.10874286, 33.30480288]),
            np.array([10.49489667, -2.26817846, 8.34242713, 7.51864081, 18.55109905, -11.95799235]),
            np.array([9.96147375, -2.43783366, 6.77865569, 8.51894855, 25.08135411, -9.88074002]),
            np.array([8.81908456, 28.13228486, 4.19898269, -24.92626711, 18.0357215, 15.58033777]),
            np.array([-6.09417553, 33.64001718, 9.83160608, -24.59861931, 17.81096035, 11.9360692]),
            np.array([8.86333358, -1.87806094, 7.02717652, 5.84762321, 23.37016425, -11.98736216]),
            np.array([-99.95877459, 33.40215818, -11.49670015, -4.51793941, 12.81024003, 32.45332438]),
            np.array([7.77184479, 29.83770008, 2.22272192, -25.36179661, 23.75672406, 10.69634763]),
            np.array([12.40089624, -3.20836511, 6.58254365, 5.93935541, 23.11953917, -12.01536404]),
            np.array([-97.34527297, 31.79681679, -11.64276809, -2.97682901, 13.13279683, 30.67622855]),
            np.array([1.09642176, 17.32216015, 6.01590742, -23.63899451, 19.63007792, 12.38437483]),
            np.array([11.94783265, -4.69617121, 4.54828529, 11.58502171, 21.19918068, -15.55934081]),
            np.array([-5.55484431, 25.124671, -3.43951269, -19.79641331, 28.66566544, 6.52540885]),
            np.array([11.27626718, -8.68672898, 4.94695138, 6.93184401, 26.37492536, -11.28799636]),
            np.array([-99.70679989, 31.17238358, -8.56535281, -4.88601551, 14.83750634, 27.88194449]),
            np.array([-1.26761808, 31.81156589, 4.01909647, -15.31768191, 19.68807786, 11.46808064]),
            np.array([-5.29064681, 22.92938866, 8.59036587, -12.37669321, 15.83744708, 17.43411975]),
            np.array([11.77813863, -0.733798, 9.69869066, 8.69604714, 23.04711651, -8.95450695]),
            np.array([0.9644018, 26.28979576, -2.30053382, -17.11908191, 28.92471481, 11.51832801]),
            np.array([21.08567711, -1.28319225, 0.14993597, 1.51560535, -2.67028591, -5.46959854]),
            np.array([10.55548811, -3.80300779, 4.78854214, 9.909941, 25.12041449, -11.38592995]),
            np.array([0.1314592, 26.42033233, 9.20581576, -15.84271951, 22.43351666, 11.35126463]),
            np.array([22.31046883, 0.58011643, -0.33850245, 4.24324507, -3.56410191, -4.59194006]),
            np.array([9.93611707, -5.71540592, 4.79410578, 8.72066271, 25.82245545, -13.64013737]),
            np.array([21.16711446, -1.27175563, -2.32234856, 6.51585207, -2.24770921, -3.80140057]),
            np.array([14.6414396, -1.9393585, 7.13311209, 11.82947749, 26.49020291, -9.09520254]),
            np.array([12.96664985, -4.07886238, 11.55353093, 9.44270331, 22.88192637, -12.99331196]),
            np.array([-99.55158341, 29.25943434, -8.31545502, -7.48487621, 15.35890765, 33.75327779]),
            np.array([-102.02418523, 31.19694923, -15.2898541, -2.96442901, 15.29673843, 32.46031795]),
            np.array([12.22920354, -2.87429068, 4.55949828, 6.25133361, 22.46672807, -12.54291554]),
            np.array([0.84272372, 20.42228273, 9.56021867, -12.09190071, 28.27596255, 4.79188684]),
            np.array([7.14454063, 27.76186295, -11.57917768, -24.74125931, 13.44154875, 15.53157623]),
            np.array([8.90655807, -3.67369406, 8.49565571, 10.57136231, 21.58445566, -10.13931849]),
            np.array([25.82239854, -2.31512855, -2.10310102, 3.56433846, -5.48621731, -3.57949626]),
            np.array([2.33662287, 29.64811404, 8.64238303, -15.08488541, 15.40103744, 6.98555396]),
            np.array([19.19121916, -0.33273085, 1.20942993, 1.33898254, -0.97438641, -5.7223575]),
            np.array([-0.07342352, 28.40709021, 10.06123961, -25.70535881, 24.96339393, 8.47231889]),
            np.array([21.36065791, -0.98272687, -1.25068473, 3.62406595, -0.97342821, -5.39433327]),
            np.array([-97.15370214, 34.84430649, -8.61759271, -6.57750341, 14.93951415, 31.58081977]),
            np.array([23.20085723, -0.07260775, -2.62945921, 4.33815171, -6.18170071, -5.4328537]),
            np.array([8.53023629, -4.88923058, 7.65096265, 10.77405091, 27.67379834, -13.95410393]),
            np.array([24.2495692, 0.80950991, -1.58523442, 4.26398181, 1.34806991, -4.6185169]),
            np.array([11.76990363, -4.59225403, 7.30355774, 6.88530841, 18.0630557, -12.1701117]),
            np.array([20.78745748, -1.5532964, 1.9086283, 9.78254568, -5.62291321, -1.26600338]),
            np.array([11.44459781, -3.8401209, 6.85168664, 9.18358221, 22.75945275, -13.37589301]),
            np.array([13.44169353, -3.10571274, 6.5307838, 6.20269481, 23.56077015, -13.138938]),
            np.array([14.76940074, -5.33201815, 6.27504882, 6.76765531, 26.45566977, -13.55018202]),
            np.array([-100.52534239, 33.27501979, -9.97155597, -4.31767731, 15.10051924, 30.26587654]),
            np.array([24.35284886, -0.69653502, -0.10611421, 4.50032546, -1.45552321, 0.37461227]),
            np.array([-102.16388798, 33.04015625, -8.1790171, -6.45979901, 12.50377037, 31.84962877]),
            np.array([5.71092863, 21.06766651, -2.02189863, -16.60584611, 7.69048664, 9.74709715]),
            np.array([-98.0605579, 32.2934801, -5.55512511, -5.64581021, 15.42019923, 31.01423637]),
            np.array([2.4628001, 25.01099814, 7.59405226, -14.2798571, 17.3843755, 8.13284581]),
            np.array([-99.45354198, 28.46270424, -11.42561869, -5.8597871, 11.49592499, 29.34055608]),
            np.array([7.58908675, 15.01303318, 7.00556071, -27.21934451, 28.02447295, 10.63892289]),
            np.array([2.66230751, 27.88170932, 1.11746333, -22.82591901, 15.40097402, 5.16208079]),
            np.array([10.78202371, -2.20350043, 7.66757553, 8.04947811, 20.65902955, -11.93157512]),
            np.array([-4.90031881, 21.27243387, 7.31818035, -26.54027721, 17.2234159, 12.57791331]),
            np.array([21.49961195, 0.0855223, 0.18994894, 3.05987964, 0.32215321, -1.80078383]),
            np.array([14.34100891, -5.52917639, 6.77764636, 4.81738441, 22.05816652, -10.14994091]),
            np.array([3.19032774, 19.17736126, 10.68898813, -18.50473601, 17.89572156, 10.46808059]),
            np.array([4.44137239, 29.7066988, 1.11914349, -19.41540341, 21.25631137, 14.38067263]),
            np.array([-98.0013242, 28.63383325, -8.86146846, -4.26699241, 13.23207887, 31.89017812]),
            np.array([14.44761845, -3.31125332, 9.02513679, 8.89538091, 23.89242774, -12.24025855]),
            np.array([20.32541142, -2.27975428, -0.21952364, 1.68155522, 0.22857801, -8.35351128]),
            np.array([-105.52211684, 34.10406658, -7.12568866, -5.10462601, 12.96804067, 30.6436943]),
            np.array([-1.44846167, 29.92683704, 8.67189807, -21.72442351, 12.47100631, 9.77406501]),
            np.array([20.10455306, 1.08365383, -0.39516354, 0.96694873, -3.33104741, -2.24860894]),
            np.array([11.84991671, -2.79580172, 8.94576342, 5.47039101, 23.14793108, -14.05081622]),
            np.array([-102.6034243, 34.3050797, -8.48883498, -4.37525111, 14.21684561, 31.64464637]),
            np.array([24.64117477, -0.62289866, 0.78647755, 4.5520144, -2.97395251, -4.38787763]),
            np.array([10.99128235, -2.44048021, 8.73969715, 4.24938481, 22.76496121, -12.0914602]),
            np.array([11.60562265, -5.25317522, 5.98932991, 8.12049001, 24.58053704, -10.0968488]),
            np.array([13.31376164, -5.45182423, 5.27556211, 8.7823021, 22.14758294, -10.16061436]),
            np.array([-95.83469272, 33.99154196, -13.82539332, -5.57204621, 10.90773881, 30.48106199]),
            np.array([-0.76387537, 26.38354138, -2.41846373, -25.56896401, 16.82050699, 16.95555178]),
            np.array([-2.14765985, 26.90280614, 3.89710861, -28.61761841, 21.92492101, 11.34515354]),
            np.array([13.83721434, -5.69560112, 12.08991525, 6.92204311, 23.74489275, -10.38521379]),
            np.array([15.76268706, -5.23636783, 4.65454193, 6.20323494, 24.63182701, -9.71900456]),
            np.array([-99.76338988, 30.48693249, -12.22863373, -5.11773201, 12.93644148, 28.71984549]),
            np.array([19.64519777, -4.3724152, 1.54998179, -0.10053908, -3.92040051, -4.92926823]),
            np.array([5.13179724, 27.09705695, 4.33834749, -21.99216771, 23.58806665, 11.6215646]),
            np.array([14.83209254, -1.83590967, 12.87980944, 7.01613081, 23.15237915, -13.98829992]),
            np.array([21.99996232, -3.59198888, 0.35558222, 2.3853501, -2.30066911, -5.17059861]),
            np.array([-2.17507473, 26.41506093, -0.4257154, -29.94384641, 26.79133682, 10.84916397]),
            np.array([-1.48951689, 27.33794098, 2.18165649, -9.66418414, 21.83295051, 16.92551519]),
            np.array([21.74317583, 0.75006905, -2.70592131, 0.05364183, -0.73484651, -8.67484869]),
            np.array([-101.31911009, 29.95559841, -9.01630131, -6.83609351, 14.36297927, 32.11266839]),
            np.array([15.13439941, -4.99066536, 11.8220435, 11.18909327, 22.28820311, -9.0050715]),
            np.array([-100.33780499, 30.75530494, -9.41858537, -7.49490811, 12.68966462, 33.67379447]),
            np.array([3.21858153, 19.74885605, 7.23566035, -25.51749711, 22.070745, 15.43452483]),
            np.array([11.97946653, -3.18293615, 9.35955762, 8.47403131, 22.60302062, -12.33828476]),
            np.array([13.67859611, -9.16209828, 6.59254792, 7.98541161, 22.0828982, -13.15116057]),
            np.array([12.77139558, -1.74844212, 4.75535077, 8.35225273, 24.46813001, -9.87753278]),
            np.array([22.90640947, -0.07910906, -1.15617247, 6.01990485, -3.01381731, -5.25175376]),
            np.array([-2.29388967, 22.55025779, -1.50641366, -21.86749631, 20.48214106, 14.25618176]),
            np.array([-97.80934214, 32.91092695, -7.9543394, -4.81806671, 12.37693946, 32.16650246]),
            np.array([-98.72647625, 33.63216063, -12.30439351, -5.87077651, 12.15460585, 29.07995193]),
            np.array([-95.66320795, 33.32312368, -11.64784422, -9.31942401, 17.44957686, 28.91950479])
        ]

    def test_fit_separated_data(self):
        """Test the fit on well-separated data."""

        # arrange
        test_data = [
            np.array([ 1.0,  3.0,  4.0]),  # cluster A
            np.array([ 1.0,  3.1,  4.0]),  # cluster A
            np.array([-1.0, -5.0,  0.0]),  # cluster B
            np.array([-1.1, -4.9, -0.1]),  # cluster B
            np.array([ 0.9,  2.9,  4.2]),  # cluster A
            np.array([ 1.1,  3.0,  3.9]),  # cluster A
            np.array([-1.0, -5.3,  0.2])   # cluster B
        ]

        test_num_clusters = 2

        expected_centers = np.array([
            [1.0, 3.0, 4.025],                      # cluster A (larger)
            [-1.03333333, -5.06666667, 0.03333333]  # cluster B (smaller)
        ])
        expected_n_clusters = 2

        # act
        test_kmeans = KMeans()

        output = test_kmeans.sorted_kmeans_fit(test_data, test_num_clusters)

        # assert
        # Compare returned centers to expected:
        self.assertEqual(output.shape, expected_centers.shape)

        for c_index in range(len(output)):
            actual_center = output[c_index]
            expected_center = expected_centers[c_index]

            for f_index in range(len(actual_center)):
                actual_value = actual_center[f_index]
                expected_value = expected_center[f_index]

                self.assertAlmostEqual(actual_value, expected_value, places=6)

        # Compare centers stored on kmeans to expected:
        self.assertEqual(test_kmeans.centers.shape, expected_centers.shape)

        for c_index in range(len(test_kmeans.centers)):
            actual_center = test_kmeans.centers[c_index]
            expected_center = expected_centers[c_index]

            for f_index in range(len(actual_center)):
                actual_value = actual_center[f_index]
                expected_value = expected_center[f_index]

                self.assertAlmostEqual(actual_value, expected_value, places=6)

        self.assertEqual(test_kmeans.n_clusters, expected_n_clusters)

    def test_fit_separated_data_100_times(self):
        """
        Repeat previous test 100 times to find issues due to randomness.
        """

        for i in range(100):
            self.test_fit_separated_data()

    def test_fit_larger_data(self):
        """
        Test the fit with a larger number of data points.
        Note that the test points are random pertubations around the following means, with the given # of points:
         - A: [ 12. ,  -3.2,   7.4,   7.5,  23.2, -12.7] (100 points)
         - B: [22. ,  0. ,  0. ,  3.7, -1.2, -5. ] (50 points)
         - C: [  0. ,  26. ,   4.3, -21. ,  19.7,  12.3] (75 points)
         - D: [-100. ,   32.1,  -10.2,   -5. ,   13.3,   31.1] (55 points)

        Using the SciKit K-Means with Kmeans++ init over 1000 iterations yields the following cluster centers. (These
        centers are consistent within about 10^-25 over all 1000 iterations.) We've sorted them here based on what
        their relative sizes should be (given number of points in each, above):
        A: [ 12.01783259,  -3.53969932,   7.45475854,   7.71900299, 23.00537837, -12.51676054]
        C: [  0.44777485,  25.57186705,   4.29238168, -21.41116058, 19.76324439,  12.58011386]
        D: [-99.89645717,  32.03632508, -10.45183845,  -5.29601688, 13.30564837,  30.91902548]
        B: [ 22.13956419,  -0.53350258,  -0.30612162,   3.5244427, -1.39324011,  -4.92974363]

        Consequentially, we should be able to use these as the expected centers learned by our KMeans as well.
        """

        # arrange
        test_num_clusters = 4

        expected_centers = np.array([
            [12.01783259, -3.53969932, 7.45475854, 7.71900299, 23.00537837, -12.51676054],     # A (100 points)
            [0.44777485, 25.57186705, 4.29238168, -21.41116058, 19.76324439, 12.58011386],     # C (75 points)
            [-99.89645717, 32.03632508, -10.45183845, -5.29601688, 13.30564837, 30.91902548],  # D (55 points)
            [22.13956419, -0.53350258, -0.30612162, 3.5244427, -1.39324011, -4.92974363]       # B (50 points)
        ])
        expected_n_clusters = 4

        # act
        test_kmeans = KMeans()

        output = test_kmeans.sorted_kmeans_fit(self.large_test_data, test_num_clusters)

        # assert
        # Compare returned centers to expected:
        self.assertEqual(output.shape, expected_centers.shape)

        for c_index in range(len(output)):
            actual_center = output[c_index]
            expected_center = expected_centers[c_index]

            for f_index in range(len(actual_center)):
                actual_value = actual_center[f_index]
                expected_value = expected_center[f_index]

                self.assertAlmostEqual(actual_value, expected_value, places=6)

        # Compare centers stored on kmeans to expected:
        self.assertEqual(test_kmeans.centers.shape, expected_centers.shape)

        for c_index in range(len(test_kmeans.centers)):
            actual_center = test_kmeans.centers[c_index]
            expected_center = expected_centers[c_index]

            for f_index in range(len(actual_center)):
                actual_value = actual_center[f_index]
                expected_value = expected_center[f_index]

                self.assertAlmostEqual(actual_value, expected_value, places=6)

        self.assertEqual(test_kmeans.n_clusters, expected_n_clusters)

    def test_fit_larger_data_100_runs(self):
        """Run the previous test 100 times to check for variability."""

        for i in range(100):
            self.test_fit_larger_data()

    def test_fit_larger_data_3_clusters(self):
        """
        Repeat the original large data test above, but with only 3 clusters.
        As before, we ran SKLearn KMeans 1000 times to find the centers.
        """

        # arrange
        test_num_clusters = 3

        expected_centers = np.array([
            [15.39174312, -2.53763374, 4.86779849, 6.32081623, 14.87250554, -9.9877549],      # A + B (150 points)
            [0.44777485, 25.57186705, 4.29238168, -21.41116058, 19.76324439, 12.58011386],    # C (75 points)
            [-99.89645717, 32.03632508, -10.45183845, -5.29601688, 13.30564837, 30.91902548]  # D (55 points)
        ])
        expected_n_clusters = 3

        # act
        test_kmeans = KMeans()

        output = test_kmeans.sorted_kmeans_fit(self.large_test_data, test_num_clusters)

        # assert
        # Compare returned centers to expected:
        self.assertEqual(output.shape, expected_centers.shape)

        for c_index in range(len(output)):
            actual_center = output[c_index]
            expected_center = expected_centers[c_index]

            for f_index in range(len(actual_center)):
                actual_value = actual_center[f_index]
                expected_value = expected_center[f_index]

                self.assertAlmostEqual(actual_value, expected_value, places=6)

        # Compare centers stored on kmeans to expected:
        self.assertEqual(test_kmeans.centers.shape, expected_centers.shape)

        for c_index in range(len(test_kmeans.centers)):
            actual_center = test_kmeans.centers[c_index]
            expected_center = expected_centers[c_index]

            for f_index in range(len(actual_center)):
                actual_value = actual_center[f_index]
                expected_value = expected_center[f_index]

                self.assertAlmostEqual(actual_value, expected_value, places=6)

        self.assertEqual(test_kmeans.n_clusters, expected_n_clusters)

    def test_kmeans_predict_spread_out(self):
        """
        Test predicting cluster of relatively spread-out data points, using centers from first test.
        """

        # arrange
        # Test data is 10 points around [1.0, 3.0, 4.0], then 10 around [-1.0, -5.0, 0.0]
        test_data = [
            np.array([0.59502503, 2.93853518, 3.92665024]),
            np.array([1.56350025, 3.11147546, 5.02235095]),
            np.array([0.985042, 3.32465998, 2.92107992]),
            np.array([1.47863926, 3.16849915, 3.63236661]),
            np.array([0.76310593, 2.85090404, 3.52053754]),
            np.array([0.5325147, 3.2473839, 3.99493572]),
            np.array([1.47285268, 3.11158601, 3.09612582]),
            np.array([0.89848385, 2.47090131, 4.30783622]),
            np.array([0.94689814, 3.54121233, 3.55144982]),
            np.array([0.51633148, 3.59166248, 3.65875335]),
            np.array([-1.13844203, -4.1379935, 0.95236739]),
            np.array([-1.10655832, -4.22839025, 0.33853854]),
            np.array([-1.25940745, -4.59524502, 0.2006862]),
            np.array([-0.68189981, -4.94028891, 0.04290731]),
            np.array([-1.24062676, -4.81273109, 0.5861373]),
            np.array([-0.78907316, -6.0082733, 0.04518856]),
            np.array([-0.49955969, -4.71232819, -0.33591087]),
            np.array([-1.71292959, -4.7340269, -0.84494996]),
            np.array([-0.95782593, -5.2394523, 0.46036315]),
            np.array([-1.55543817, -5.72755686, 0.20253697])
        ]

        test_centers = np.array([
            [1.0, 3.0, 4.025],                      # cluster A (larger)
            [-1.03333333, -5.06666667, 0.03333333]  # cluster B (smaller)
        ])

        # First 10 points go into cluster 0, second 10 go into cluster 1
        expected_output = np.array([
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
        ])

        # act
        test_kmeans = KMeans()

        output = test_kmeans.sorted_kmeans_predict(test_data, test_centers)

        # assert
        self.assertEqual(output.shape, expected_output.shape)

        for i in range(len(output)):
            actual_value = output[i]
            expected_value = expected_output[i]

            self.assertEqual(actual_value, expected_value)
