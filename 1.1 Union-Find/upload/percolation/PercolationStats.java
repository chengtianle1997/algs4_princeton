import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {

    private final double[] openrate;
    private final int Trails;
    private static final double CONFIDENCE_95 = 1.96;

    // perform independent trials on an n-by-n grid
    public PercolationStats(int n, int trials) {
        // check the input param
        if (n <= 0 || trials <= 0)
            throw new IllegalArgumentException();
        Trails = trials;
        openrate = new double[Trails];
        for (int i = 0; i < trials; i++) {
            Percolation perco = new Percolation(n);
            int count = 0;
            while (!perco.percolates()) {
                int row = StdRandom.uniform(1, n + 1);
                int col = StdRandom.uniform(1, n + 1);
                if (!perco.isOpen(row, col)) {
                    perco.open(row, col);
                    count = count + 1;
                }
            }
            openrate[i] = (double) count / (n * n);
        }
    }

    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(openrate);
    }

    // sample  standard deviation of percolation threshold
    public double stddev() {
        return StdStats.stddev(openrate);
    }

    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - CONFIDENCE_95 * stddev() / Math.sqrt(Trails);
    }

    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + CONFIDENCE_95 * stddev() / Math.sqrt(Trails);
    }

    // test client
    public static void main(String[] args) {
        int n = 0, trails = 0;
        // check the input param
        try {
            n = Integer.parseInt(args[0]);
            trails = Integer.parseInt(args[1]);
        } catch (NumberFormatException e) {
            StdOut.println("Input Error Occurs!");
        }
        PercolationStats persta = new PercolationStats(n, trails);
        StdOut.println("mean                     =   " + persta.mean());
        StdOut.println("stddev                   =   " + persta.stddev());
        StdOut.println("95% confidence interval  =  [" + persta.confidenceLo() + ",  " + persta.confidenceHi() + "]");
    }
}
