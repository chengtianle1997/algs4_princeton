public class Percolation {

    // arrays for quick-uf with weighting and path compression
    private int[] id;
    private int[] sz;
    private int opensites = 0;
    private boolean[] open;
    private final int N;
    private final int size;
    // no virtual bottom union-find to avoid backwash
    private int[] idNoneBottom;
    private int[] szNoneBottom;

    // create n-by-n grid, with all sites initially blocked
    public Percolation(int n) {
        // check the input param
        if (n <= 0)
            throw new IllegalArgumentException();
        N = n;
        size = n * n + 2;
        id = new int[size];
        sz = new int[size];
        open = new boolean[size];
        // no virtual bottom union-find to avoid backwash
        idNoneBottom = new int[size - 1];
        szNoneBottom = new int[size - 1];
        // initialize all the arrays
        for (int i = 0; i < size; i++) {
            sz[i] = 1;
            open[i] = false;
            id[i] = i;
            if (i != (size - 1)) {
                idNoneBottom[i] = i;
                szNoneBottom[i] = 1;
            }
        }
        open[0] = true;
        open[n * n + 1] = true;
    }

    private int root(int i) {
        while (id[i] != i) {
            i = id[i];
            // path compression
            id[i] = id[id[i]];
        }
        return i;
    }

    private void union(int i, int j) {
        int root_i = root(i);
        int root_j = root(j);
        if (sz[root_i] < sz[root_j]) {
            id[root_i] = root_j;
            sz[root_j] += sz[root_i];
        } else {
            id[root_j] = root_i;
            sz[root_i] += sz[root_j];
        }
    }

    private boolean connected(int i, int j) {
        return root(i) == root(j);
    }

    //union-find with no virtual bottom
    private int rootNoneBottom(int i) {
        while (idNoneBottom[i] != i) {
            i = idNoneBottom[i];
            // path compression
            idNoneBottom[i] = idNoneBottom[idNoneBottom[i]];
        }
        return i;
    }

    private void unionNoneBottom(int i, int j) {
        int root_i = rootNoneBottom(i);
        int root_j = rootNoneBottom(j);
        if (szNoneBottom[root_i] < szNoneBottom[root_j]) {
            idNoneBottom[root_i] = root_j;
            szNoneBottom[root_j] += szNoneBottom[root_i];
        } else {
            idNoneBottom[root_j] = root_i;
            szNoneBottom[root_i] += szNoneBottom[root_j];
        }
    }

    private boolean connectedNoneBottom(int i, int j) {
        return rootNoneBottom(i) == rootNoneBottom(j);
    }

    private int[] find_neighbor(int i) {
        int[] neighbors = {-1, -1, -1, -1};
        // if it is the right line
        if (i % N != 0)
            neighbors[0] = i + 1;
        // if it is the left line
        if ((i % N) != 1)
            neighbors[1] = i - 1;
        // if it is the top line
        if (i > N)
            neighbors[2] = i - N;
        else
            neighbors[2] = 0;
        // if it is the bottom line
        if (i <= N * (N - 1))
            neighbors[3] = i + N;
        else
            neighbors[3] = N * N + 1;
        return neighbors;
    }

    private void isValid(int row, int col) {
        if (row > N || row < 1 || col > N || col < 1)
            throw new IllegalArgumentException();
    }

    // open the site (row, col) if it is not open already
    public void open(int row, int col) {
        isValid(row, col);
        int index = (row - 1) * N + col;
        if (!open[index]) {
            int[] neighbors;
            open[index] = true;
            opensites += 1;
            neighbors = find_neighbor(index);
            for (int i = 0; i < 4; i++) {
                if (neighbors[i] >= 0) {
                    if (open[neighbors[i]]) {
                        union(neighbors[i], index);
                        // union-find with no virtual bottom
                        if (neighbors[i] != (size - 1)) {
                            unionNoneBottom(neighbors[i], index);
                        }
                    }

                }
            }
        }
    }

    // is the site (row, col) open?
    public boolean isOpen(int row, int col) {
        isValid(row, col);
        return open[(row - 1) * N + col];
    }

    // is the site (row, col) full?
    public boolean isFull(int row, int col) {
        isValid(row, col);
        return connectedNoneBottom((row - 1) * N + col, 0);
    }

    // returns the number of open sites
    public int numberOfOpenSites() {
        return opensites;
    }

    // does the system percolate?
    public boolean percolates() {
        return connected(0, size - 1);
    }

}
