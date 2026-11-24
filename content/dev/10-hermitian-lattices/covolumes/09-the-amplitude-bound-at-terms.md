---
title: The amplitude bound at terms
decls:
  - GlobalTheory.TypeAsm.AmpTerms.amplitudeBound_of_localData_of_tailBound
  - GlobalTheory.T.amplitudeBound_at_terms_of_localData
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The amplitude bound at terms

The type bound of the [next section](/entry/type-bound-of-gap/) has two halves: a bound for the amplitude of each relevant term, and a bound for the weighted number of pairs of terms. This section proves the first half. The amplitude of a term is a global orbital integral. It factors as the covolume of an integral stabilizer times a product of local amplitudes over the infinite places. The covolume is bounded by the weight of the term, through the [covolume of the reference lattice stabilizer](/entry/covol-ref/), and each local amplitude is bounded by the [Hilbert-Schmidt bound](/entry/sqrt-hs-norm-sq-amplitude-le-deg-bd/) of the degenerate amplitude.

We work in the setting of the type bound. A datum $D$ fixes the host CM field $E$ with $f$ infinite places, the ranks $k$, $r$ and $m = 2r + 2$, and the constant $v$ of $E$. Size data fix a large parameter $b$. A setting $X$ and a family $Y$ of term operators are given, and $u$ is a word. For each relevant term $t$ of $(Y, u)$ we have: the norm $\|a_t\|$ of its vector in the term operator, a counting weight $\mathrm{wt}(t) \ge 0$, an index $j(t)$ and a label $\delta(t)$, and its weight $\omega(t) = \omega_{\inf}$, the infimum of the weights $\omega_N(\Lambda_t)$ over the normal forms $N$ adapted to the two flags of $t$ (see [the frame class section](/entry/sum-cls-om-le-dat-bd/)). Let $d_\pi(u)$ be the product over the infinite places of the dimensions of the local Bessel spaces, and let $A(C_H, C_s, C; j, \delta)$ be the amplitude factor of the type bound.

**Definition 2.9.1 (Amplitude bound).** The amplitude bound is the following statement. For all constants $C_g, c_b, C_w, c_T, C_T, C_0$ with $c_b > 0$ and $c_T > 0$ there is $C_H \ge 0$ such that for every $C_s \ge 0$ there is $C_\ast \ge 0$ such that for every $C \ge C_\ast$ there are $C'_\ast, C_{l\ast}$ such that for all $C' \ge C'_\ast$ and $C_l \ge C_{l\ast}$ the following holds. For every datum $D$ with ties, size data satisfying the $k_2$ hypotheses with the constants $(C', C_l, C_g, c_b, C_w, c_T, C_T, C_0)$, every setting $X$, every family $Y$ with the concentration tie, every word $u$ and every relevant term $t$,
$$\|a_t\| \le \mathrm{wt}(t)\, \sqrt{d_\pi(u)}\; \omega(t)\, A(C_H, C_s, C; j(t), \delta(t)).$$

**Definition 2.9.2 (Local data and tail bounds).** The local data statement says: for every datum $D$ and setting $X$ with at least one word, the gap hypothesis and the signature tie, there is a choice of local data at the infinite places with Bessel vectors that are good for every pair of words. The tail statement says: for all constants as above there is $C_H \ge 0$ such that for every $C_1 \in \mathbb{N}$ there are thresholds $C'_\ast, C_{l\ast}$ beyond which every datum with ties, the $k_2$ hypotheses and large traces has Bessel functions with tail bounds of order $C_1 k r$ and scale $H_1(C_H)$ at every infinite place.

**Theorem 2.9.3 (Amplitude bound at terms).** The local data statement and the tail statement imply the amplitude bound.

Lean: `GlobalTheory.TypeAsm.AmpTerms.amplitudeBound_of_localData_of_tailBound` (also `GlobalTheory.T.amplitudeBound_at_terms_of_localData`, a second name).

*Proof.* Fix the constants. The tail statement gives $C_H$. Let $C_s \ge 0$. A product bound over the places gives a natural number $C_1 \ge 1$ and, for each relevant term, minor bounds $D_{e,\tau}$ at the places $\tau$ with a bound $P$ on the product of the local degree bounds. An arithmetic lemma gives a constant $C_a$, and we put $C_\ast = \max(C_a, 0)$. For $C \ge C_\ast$ the tail statement at $C_1$ gives thresholds $C'_1, C_{l1}$, and the gap statement gives a threshold $C_{lg}$. We take $C'_\ast = \max(C'_1, 40)$ and $C_{l\ast} = \max(C_{l1}, C_{lg}, 1)$.

Now fix the data. The $k_2$ hypotheses give the sizes: $m = 2r + 2$, $v \ge 1$, $2v \le b$, $f \ge 1$, $k \ge 40 r^4$, $k \ge 5r$, and every word has positive trace. They also give the gap hypothesis. So the local data statement gives good local data, and the tail statement gives tail bounds at every place. The integral unipotent group of the setting has finite covolume, bounded below in the form $1 \le V \cdot L$ that the chain of inequalities at the end needs.

Let $t$ be a relevant term. Then $1 \le j(t) \le r$. Put
$$c = \mathrm{wt}(t)\, \sqrt{d_\pi(u)}\, A(C_H, C_s, C; j(t), \delta(t)).$$
Since some adapted normal form exists and $\omega(t)$ is the infimum over adapted normal forms, it suffices to prove $\|a_t\| \le c\, \omega_N(\Lambda_t)$ for each normal form $N$ adapted to $t$.

Fix such an $N$. Its index is $j(t)$. At each infinite place $\tau$ the term gives an element $\gamma_\tau$ with $\gamma_\tau^{-1} = n_1 g n_2$, where $n_1, n_2 \in N$ and $g$ is normal with data $(j(t), \beta, c_\tau)$. So the image $\mu_\tau$ of $\mu^0_\beta$ under conjugation by $n_2^{-1}$ is a normal-form stabilizer measure for $\gamma_\tau^{-1}$ with scale $1$. Each $\mu_\tau$ has a quotient measure $\nu_\tau$. There is a strict fundamental set $K$ for the integral stabilizer of the term, and the covolume theorem gives
$$\Bigl(\prod_\tau \mu_\tau\Bigr)(K) \le \omega_N(\Lambda_t)\, v^{k(r-j)f}\, \ell(D),$$
where $\ell(D)$ is an explicit loss factor. The unfolding of the global orbital integral gives
$$\|a_t\| \cdot V \le \mathrm{wt}(t) \cdot \Bigl(\prod_\tau \mu_\tau\Bigr)(K) \cdot \prod_\tau \|J_\tau\|_{\mathrm{HS}},$$
where $J_\tau$ is the local amplitude of $\gamma_\tau$.

We bound each $\|J_\tau\|_{\mathrm{HS}}$ by the Hilbert-Schmidt theorem with both words equal to $u$, $\theta = 1$, $s = 1$, $H_1 = H_1(C_H) \ge 1$ and $q = C_1 k r$. The theorem needs $j + 2 \le k$ and $16 r^3 + 4r + 2 \le q$. Both follow from $k \ge 40 r^4$ and $r \ge 1$: for instance $16 r^3 + 4r + 2 \le 40 r^5 \le k r \le C_1 k r$. The product of the factors $\sqrt{\dim W_{p,\tau}}$ is $\sqrt{d_\pi(u)}$, the product of the factors $\kappa_1 = (2v)^{-rk} 2^{r(k+1)+r(r-1)}$ is $\kappa_1^f$, and the product of the degree bounds is at most $P$. So
$$\prod_\tau \|J_\tau\|_{\mathrm{HS}} \le \sqrt{d_\pi(u)}\, \kappa_1^f\, P.$$

Finally combine the three bounds. Multiply the unfolding inequality by $L$ and use $1 \le V L$. The arithmetic lemma of the first step says that $v^{k(r-j)f} \ell(D)\, L^2\, \kappa_1^f\, P$ is at most $A(C_H, C_s, C; j(t), \delta(t))$ under the size conditions, for $C \ge C_a$. This gives $\|a_t\| \le c\, \omega_N(\Lambda_t)$. $\square$

**Remark 2.9.4.** The main factor of the covolume, $v^{k(r-j)f}$, and the factor $(2v)^{-rkf}$ of $\kappa_1^f$ nearly cancel. The amplitude bound is therefore of the size of the weight times the product of the local degree bounds, which decay in the minors of the term.

**Remark 2.9.5 (Formalization).** The objects of the setting (`D7`, `SizeData₂`, `HidaSetting`, `Full`, `relSet`, `k2a`, `dpiC`, `wt`, `omT`) are defined in other chapters and are used here through their names; the text describes them in words. The three statements are the propositions `AmpP`, `LocDatC` and `TailP`. The proof uses the local lemmas `chain`, `sizes`, `prod_bound` and `prod_sqrt` ([AmplitudeBoundAtTermsOfLocalData.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplitudeBoundAtTermsOfLocalData.lean#L49)) for the arithmetic, and the results `integralStabiliser_covolume_le_indexWeight` and `termAmplitude_le_covolume_localAmplitudes` for the covolume and the unfolding. The concentration tie is used twice: one of its components gives the trace condition of the tail statement, and it gives $j(t) \ge 1$ (`JPosC_holds`). The Hilbert-Schmidt theorem is applied with the same word $u$ on both sides. The second name is a wrapper of the form `first | exact @X | exact X | ...`.
