from load_data import load

def load_datasets():
    X_train, X_train_candidates, Y_train = load('train/in.tsv', 'train/expected.tsv')
    X_dev, X_dev_candidates, Y_dev = load('dev-0/in.tsv', 'dev-0/expected.tsv')
    X_test, X_test_candidates, _ = load('test-A/in.tsv', 'test-A/out.tsv')
    return X_train, X_train_candidates, Y_train, X_dev, X_dev_candidates, Y_dev, X_test, X_test_candidates
