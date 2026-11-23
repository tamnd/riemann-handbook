---
title: The arithmetic volume of bundles nef on the fibres
decls:
  - GlobalTheory.GenFibreGen.exists_secs_generic
  - GlobalTheory.T.exists_sections_nefPlusAmple_generated_genericFibre
  - GlobalTheory.VolBr.exists_isNef_shift_pow_tens
  - GlobalTheory.T.exists_metricShift_isNef_pow_tens_ample
  - GlobalTheory.VolBr.volGe_of_hilbertSamuel
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The arithmetic volume of bundles nef on the fibres

The arithmetic Hilbert-Samuel formula of [the previous section](/entry/arith-hilbert-samuel-of-principalisation/) counts the small sections of a nef bundle. This section uses it to bound the arithmetic volume of a bundle that is only semipositive and nef on the fibres: the volume is at least the self intersection. This is the inequality $\widehat{\operatorname{vol}}(\bar L) \ge \widehat{\deg}(\hat c_1(\bar L)^{D+1})$ of Moriwaki and Yuan. It is used in [the published results](/step/published-results-arithmetic/) through [the volume bound from the literature](/entry/vol-ge-of-literature/).

### Definitions

Let $X$ be an arithmetic variety of relative dimension $D$ over $k$, and let $\bar L$ be a hermitian line bundle on $X$. We use the notions of [the nef case](/entry/arith-hilbert-samuel-of-ample-hs/): small sections, nefness on the fibres, and self intersections.

**Definition 6.8.1 (Arithmetic volume).** The arithmetic volume of $\bar L$ is
$$\widehat{\operatorname{vol}}(\bar L) = \limsup_{m \to \infty} \frac{(D+1)!}{m^{D+1}} \log \#\{\text{small sections of } \bar L^m\},$$
a number in $[-\infty, +\infty]$. See the [arithmetic volume and bigness](/learn/arakelov/#arithmetic-volume-and-bigness) of Volume 1.

**Definition 6.8.2 (Volume bound).** The volume bound is the statement: for every arithmetic variety $X$ and every hermitian line bundle $\bar L$ on $X$ that is semipositive and nef on the fibres, with self intersection $a$, we have $a \le \widehat{\operatorname{vol}}(\bar L)$.

**Definition 6.8.3 (Nef numerics).** Nef numerics is the conjunction of three classical facts for projective varieties $V$ of dimension $D$ over an algebraically closed field: intersection numbers of nef line bundles are at least $0$; a nef line bundle $N$ is big if and only if $N^D > 0$; and for a nef line bundle $L$,
$$h^0(L^m) - \frac{L^D}{D!} m^D = O(m^{D-1}).$$

### Sections on the generic fibre

Let $X_{\mathbb{Q}}$ be the generic fibre of $X$ over $\mathbb{Z}$. A point $x$ of $X$ lies over $X_{\mathbb{Q}}$ if and only if its residue field has characteristic zero.

**Proposition 6.8.4 (Generated powers on the generic fibre).** Assume nef numerics. Let $\bar L$ be nef on the fibres, let $\bar A$ be a hermitian line bundle whose line bundle $A$ is ample, and let $n \ge 0$. Then there are $m \ge 1$ and finitely many global sections $s_1, \dots, s_N$ of $(L^n \otimes A)^m$ on $X$ such that every point of $X$ with residue field of characteristic zero lies outside the zero locus of some $s_i$.

Lean: `GlobalTheory.GenFibreGen.exists_secs_generic` (also `GlobalTheory.T.exists_sections_nefPlusAmple_generated_genericFibre`, a second name).

*Proof.* Powers of a bundle nef on the fibres are nef on the fibres, since the degree on a curve is multiplied by $n$. A bundle nef on every fibre over a finite field is nef on $X_{\mathbb{Q}}$; this is a result of the development, which reduces a curve on $X_{\mathbb{Q}}$ to its specialisations. So $L^n$ is nef on $X_{\mathbb{Q}}$.

The pull back of $A$ to $X_{\mathbb{Q}}$ is ample. By nef numerics a nef bundle tensored with an ample bundle is ample, so $(L^n \otimes A)_{\mathbb{Q}}$ is ample on $X_{\mathbb{Q}}$, which is projective over $\mathbb{Q}$. Some power $m \ge 1$ of it is globally generated, and since $X_{\mathbb{Q}}$ is quasi-compact, finitely many sections $v_1, \dots, v_N$ of the $m$-th power have no common zero on $X_{\mathbb{Q}}$.

Each $v_i$ is a section on the generic fibre. Multiplying by a nonzero integer clears its denominators, so some integer multiple $c_i v_i$ extends to a global section $s_i$ on $X$; this extension result is taken from the development. Multiplication by $c_i$ does not change the zero locus on $X_{\mathbb{Q}}$, where $c_i$ is a unit. A point $x$ with residue field of characteristic zero is the image of a point $y$ of $X_{\mathbb{Q}}$, and $v_i(y) \ne 0$ for some $i$, so $s_i(x) \ne 0$. $\square$

### A nef shift

For a real $t$ write $\bar M(t)$ for $\bar M$ with all norms multiplied by $e^{-t}$. Small sections of $\bar M(t)$ are the sections of norm at most $e^{t}$.

**Proposition 6.8.5 (A nef shift).** Assume the arithmetic intersection calculus and nef numerics. Let $\bar L$ be semipositive and nef on the fibres, let $\bar A$ be nef with $A$ ample, and let $n \ge 0$. Then there is a real $t$ such that $(\bar L^n \otimes \bar A)(t)$ is nef.

Lean: `GlobalTheory.VolBr.exists_isNef_shift_pow_tens` (also `GlobalTheory.T.exists_metricShift_isNef_pow_tens_ample`, a second name).

*Proof.* Put $\bar M = \bar L^n \otimes \bar A$. By [the previous proposition](/entry/exists-secs-generic/) there are $m \ge 1$ and sections $s_1, \dots, s_N$ of $M^m$ with no common zero at points of characteristic zero. The bundle $\bar M$ is semipositive, as a tensor product of semipositive bundles. It is nef on the fibres, as a tensor product of bundles nef on the fibres. A result of the development says that a semipositive bundle, nef on the fibres, with such sections, becomes nef after a shift. In outline: on a horizontal curve $Z$ some $s_i$ does not vanish identically, so $s_i|_Z$ is a rational section of $M^m|_Z$ with effective divisor. Its arithmetic degree is at least $-\sum_\sigma \sum_y \log\|s_i\|_\sigma(y)$, and after a shift by $t$ every norm $\|s_i\|$ is at most $1$, so the degree is at least $0$. The shift changes neither semipositivity nor the degrees on vertical curves. $\square$

### The volume bound

**Theorem 6.8.6 (Volume bound from the Hilbert-Samuel formula).** The arithmetic Hilbert-Samuel formula, the arithmetic intersection calculus and nef numerics imply the volume bound. That is, under these three hypotheses, if $\bar L$ is semipositive and nef on the fibres with self intersection $a$, then $a \le \widehat{\operatorname{vol}}(\bar L)$.

Lean: `GlobalTheory.VolBr.volGe_of_hilbertSamuel`.

*Proof.* By the calculus, the development gives a pair $P = (\bar L, \bar A)$ in the sense of [the ample case](/entry/tendsto-log-count-sub-up/), with $\bar A$ nef and $A$ ample, and with sections whose norms it controls. We use the counts $\operatorname{lc}(r, s, R) = \log \# H(r, s)_{\le R}$ of that section. So $\operatorname{lc}(r, 0, 1)$ is the logarithm of the number of small sections of $\bar L^r$, and $\operatorname{lc}(r, s, 1)$ that of $\bar L^r \otimes \bar A^s$. By a cited reduction, it is enough to prove: for every $\varepsilon > 0$ there are infinitely many $N$ such that the small sections of $\bar L^N$ form a finite set and
$$\log \#\{\text{small sections of } \bar L^N\} \ge \left(\frac{a}{(D+1)!} - \varepsilon\right) N^{D+1}.$$

Fix $\varepsilon > 0$. By the calculus there are self intersections $\alpha_n$ of $\bar L^n \otimes \bar A$ with $\alpha_n / n^{D+1} \to a$. The development also gives continuity of the count from above: for all large $n$ and all large $m$,
$$\operatorname{lc}(nm, m, 1) \le \operatorname{lc}(nm, 0, 1) + \tfrac{\varepsilon}{3} (nm)^{D+1}.$$
This says that tensoring with $\bar A^m$ adds few small sections when $n$ is large. Choose $n \ge 1$ for which this holds and $\alpha_n / n^{D+1} > a - \varepsilon / 3$.

By [the nef shift](/entry/exists-is-nef-shift-pow-tens/), there is $t_0$ such that $(\bar L^n \otimes \bar A)(t_0)$ is nef. The Hilbert-Samuel formula applies to this nef bundle, with self intersection $\alpha_n + (D+1) t_0 \deg(L^n \otimes A)_{\mathbb{C}}$ by the shift rule of the calculus. A result of the development turns the formula for the shifted bundle into a bound for the unshifted count: for all large $m$
$$\operatorname{lc}(mn, m, 1) \ge \left(\frac{\alpha_n}{(D+1)!} - \frac{\varepsilon}{3}\right) m^{D+1}.$$

Now take $m$ large and $N = nm$. The small sections of $\bar L^N$ form a finite set, since the balls of the development are finite. Then
$$\operatorname{lc}(N, 0, 1) \ge \operatorname{lc}(N, m, 1) - \tfrac{\varepsilon}{3} N^{D+1} \ge \left(\frac{\alpha_n}{(D+1)!} - \frac{\varepsilon}{3}\right) m^{D+1} - \frac{\varepsilon}{3} N^{D+1}.$$
Since $\alpha_n \ge (a - \varepsilon/3) n^{D+1}$, $m^{D+1} \le N^{D+1}$ and $(D+1)! \ge 1$, the right side is at least $(a/(D+1)! - \varepsilon) N^{D+1}$. There are infinitely many such $N$, since $m$ is arbitrary. $\square$

**Remark 6.8.7 (Formalization).** The volume is the upper limit of $\log$ of the extended cardinality of the set of small sections, in the extended reals, so an infinite set gives $+\infty$ ([NefFibOfIsNef.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NefFibOfIsNef.lean#L52)). The bound is stated in the extended reals. Nefness on the fibres quantifies over every finite field $\kappa$ with an algebra structure on the ring of functions of the curve, not only the residue field ([NefFibOfIsNef.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/NefFibOfIsNef.lean#L48)). The nef shift asks for $\bar A$ nef, and uses only its semipositivity and its nefness on the fibres. The good bundle $\bar A$, the reduction to infinitely many $N$, the continuity from above, the passage from nef on finite fibres to nef on the generic fibre, the extension of sections and the shift lemma are cited results whose proofs we did not open.
