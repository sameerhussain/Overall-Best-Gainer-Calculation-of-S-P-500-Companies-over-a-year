from filenames_getter import filler
from stats import stats
def main():

    f = filler()
    f.main()
    st = stats()
    st.sort_the_matter_out(st.collect_data())

if __name__=='__main__':
    main()