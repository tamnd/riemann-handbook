---
title: Series of matrix coefficients
decls:
  - GlobalTheory.KFourier.kFourier_coeff_decay
  - GlobalTheory.T.kFourier_coefficient_rapid_decay
  - GlobalTheory.KFourier.exists_rightKFourier
  - GlobalTheory.T.exists_rightKFourierSeries_unitary_moderateGrowth
  - GlobalTheory.TypeSum.TraceBound.trace_bound
  - GlobalTheory.TypeSum.CoefRep.exists_rewrite
  - GlobalTheory.T.exists_common_growth_exponent_gK_discreteSeries
  - GlobalTheory.TypeSum.KSeries.hasTypeAll_of_kTypes
  - GlobalTheory.T.discreteSeriesCoeffSeries_of_kTypeProjections
  - GlobalTheory.ClosureSeries.hasTypeAll_of_closure
  - GlobalTheory.T.hasAllKTypes_of_closure_discreteSeriesCoefficients
  - GlobalTheory.ClosureSeries.closure_model
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Series of matrix coefficients

Let $f$ be a function of moderate growth on an indefinite unitary group $G$, and let $\sigma$ be a [[discrete series|9AB7HYGPEK]] representation. Suppose that $f$ is a limit, uniformly on compact sets, of finite sums of [[matrix coefficients|J85Q7QGGHS]] of $\sigma$. We prove that $f$ is then a convergent series of matrix coefficients, with control of all Sobolev norms. The method is the Fourier expansion of $f$ along the maximal compact subgroup $K$: its terms decay rapidly, and each is a finite sum of matrix coefficients that we rewrite with a uniform bound. The result is used in the proof of [Theorem 3.6 of Volume 14](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/) on smooth cuspidal lifts.

### Groups, words and growth

Fix $n$ and a signature $\varepsilon \in \{0,1\}^n$, with diagonal matrix $J_\varepsilon$ of signs. Let $G = \{g \in M_n(\mathbb{C}) : g^* J_\varepsilon g = J_\varepsilon\}$ and $\mathfrak{g} = \{X : X^* J_\varepsilon + J_\varepsilon X = 0\}$. Let $K$ be the maximal compact subgroup of $G$ with its [[Haar measure|VY0HXD3GC4]] $dk$, and $\mathfrak{k}$ the skew-hermitian elements of $\mathfrak{g}$. Put $|y|^2 = \sum_{i,j} |y_{ij}|^2$. A *word* is a finite list of elements of $\mathfrak{g}$.

Let $\sigma$ be a representation of $G$ by bounded operators on an inner product space $\mathcal{H}$. For a word $l = (X_1, \dots, X_m)$ let $D_l = d\sigma(X_1) \cdots d\sigma(X_m)$. For a finite set $S$ of words put $\|w\|_S = \sum_{l \in S} \|D_l w\|$. We have not unfolded smooth vectors or the class of *Sobolev functionals*, which are linear forms bounded by some $\|\cdot\|_S$.

**Definition 5.8.1 (Uniform moderate growth).** A family $F_l$ of functions on $G$, indexed by words, is a *derivative family* if $\frac{d}{dt} F_l(g \exp tX)|_{t=0} = F_{(X) \cdot l}(g)$ for every word $l$, every $X \in \mathfrak{g}$ and every $g \in G$. It has *growth $N$* if for each $l$ there is $C$ with $|F_l(g)| \le C(1 + |g|^2)^N$ on $G$. A function $f$ has *uniform moderate growth* if $f = F_{()}$ on $G$ for a derivative family $F$ of some growth $N$.

**Definition 5.8.2 (Fourier kernel).** Let $P_d$ be the span of the products of at most $d$ entries of $k$ or of their conjugates, as functions on $K$, and put $P_{-1} = 0$. A *Fourier kernel of degree $i$* is an $e \in P_i$ with $\int_K e\, q\, dk = 0$ for $q \in P_{i-1}$ and $\int_K e\, p\, dk = p(1)$ for every $p \in P_i$ orthogonal to $P_{i-1}$.

A function $e$ on $K$ is *$K$-finite* if it lies in a finite-dimensional space of continuous functions that is stable under left and right translations.

**Definition 5.8.3 (Standard representation).** $\sigma$ is *standard* if it is a unitary, irreducible representation of $G$, each $K$-finite vector is smooth, $\sigma$ has a formal degree, and there is a nonzero $K$-finite vector.

**Definition 5.8.4 (Discrete series with parameter $\lambda$).** $\sigma$ is in the *discrete series with parameter $\lambda$* if $\mathcal{H}$ is complete and nonzero, $\sigma$ is unitary, irreducible and square integrable, the $K$-type with highest weight $\Lambda_\lambda$ occurs in $\sigma$, and $\|\Lambda_\lambda + 2\rho_c\| \le \|\mu + 2\rho_c\|$ for every $K$-type $\mu$ of $\sigma$.

We have not unfolded $\Lambda_\lambda$; see [discrete series](/learn/real-groups/#discrete-series-and-formal-degrees).

**Definition 5.8.5 (Coefficient series).** A function $f$ on $G$ is a *coefficient series* of $\sigma$ if there is a finite set $S$ of words with these properties:

1. there is a continuous $\beta$ with $\|\sigma(g) w\|_S \le \beta(g)\|w\|_S$ for $g \in G$ and smooth $w$;
2. there are smooth vectors $v_i$, linear forms $\ell_i$ and numbers $c_i \ge 0$ with $|\ell_i(w)| \le c_i \|w\|_S$ for smooth $w$;
3. $\sum_i c_i \|v_i\|_{S'}$ converges for every finite set $S'$ of words, including $S' = S$;
4. $f(g) = \sum_i \ell_i(\sigma(g) v_i)$ for $g \in G$.

The theorems below also assume two published results: the structure theory of [[Harish-Chandra modules|2MKHH636C3]], and the Casselman-Wallach theorem on smooth globalizations. We have not unfolded their statements.

### The right $K$-Fourier series

**Theorem 5.8.6 (Decay of $K$-Fourier coefficients).** Let $F$ be a derivative family of growth $N$ with $F_{()}$ continuous on $G$. Let $e_i$ be a Fourier kernel of degree $i$ for each $i$, and $u$ a word with letters in $\mathfrak{k}$. Then there is a summable sequence $b_i$ with
$$\Bigl|\int_K e_i(k)\, F_u(yk)\, dk\Bigr| \le b_i (1 + |y|^2)^N \qquad (i \ge 0,\ y \in G).$$

Lean: `GlobalTheory.KFourier.kFourier_coeff_decay` (also `GlobalTheory.T.kFourier_coefficient_rapid_decay`, a second name).

*Proof.* Take a finite real spanning set of $\mathfrak{k}$ and let $\Omega$ be the Casimir operator of $K$ built from it. A spectral gap lemma gives $c, \alpha > 0$ such that, for $i \ge 1$, $\Omega$ is at least $c\, i^\alpha$ on the part of $P_i$ orthogonal to $P_{i-1}$. Choose $M$ with $n^2 + 2 < \alpha M$.

A pairing lemma gives $C$ with $|\int_K \Omega^M s(k)\, F_u(yk)\, dk| \le C \|s\|_2 (1 + |y|^2)^N$ for $s \in P_i$. By the spectral gap, $e_i = \Omega^M s$ with $\|s\|_2 \le (c\, i^\alpha)^{-M} \|e_i\|_2$. Also $\|e_i\|_2^2 \le \dim P_i \le (i+1)^{2n^2}$. So for $i \ge 1$ we can take
$$b_i = |C|\, (c\, i^\alpha)^{-M} (i+1)^{n^2},$$
and $b_0$ comes from the pairing lemma with $M = 0$. Since $n^2 - \alpha M < -1$, the sequence $b_i$ is summable. $\square$

**Theorem 5.8.7 (Right $K$-Fourier series).** There are continuous, $K$-finite functions $e_i$ on $K$ with this property. Let $f$ be continuous on $G$ with uniform moderate growth. Then there are $N$, functions $\Phi_{i,l}$ on $G$ for each $i$ and word $l$, and numbers $B_{i,k}$, such that:

1. $\Phi_{i,()}(y) = \int_K e_i(k) f(yk)\, dk$ for $y \in G$;
2. $\frac{d}{dt}\Phi_{i,l}(y \exp tX)|_{t=0} = \Phi_{i,(X)\cdot l}(y)$ for $y \in G$, $X \in \mathfrak{k}$, and $l$ with letters in $\mathfrak{k}$;
3. $|\Phi_{i,w}(y)| \le B_{i,k} (1 + |y|^2)^N$ for $y \in G$ and $|w| \le k$, with letters $X \in \mathfrak{k}$ and $|X| \le 1$;
4. $\sum_i B_{i,k}$ converges for each $k$;
5. $\sum_i \int_K e_i(k) f(yk)\, dk = f(y)$ for $y \in G$.

Lean: `GlobalTheory.KFourier.exists_rightKFourier` (also `GlobalTheory.T.exists_rightKFourierSeries_unitary_moderateGrowth`, a second name).

*Proof.* A lemma gives a Fourier kernel $e_i$ of each degree. It lies in $P_i$, so it is continuous and $K$-finite. For $y \in G$ the average $a_{i,y}(x) = \int_K e_i(k) f(yxk)\, dk$ lies in $P_i$. Let $\Phi_{i,l}(y)$ be the right derivative of $a_{i,y}$ along $l$, at $1$. Then (1) holds, and (2) holds because $a_{i, y\exp tX}$ is the right translate of $a_{i,y}$ by $\exp tX$.

A lemma on $P_i$ gives, for each $k$, finitely many words $U_k$ in $\mathfrak{k}$ and $C_k \ge 0$ that bound the derivatives of order $k$ at $1$ by $C_k$ times the sum of those along $U_k$. The kernel $e_i$ is invariant under conjugation, so the derivative of $a_{i,y}$ along $u$ at $1$ is $\int_K e_i(k) F_u(yk)\, dk$. The decay theorem bounds it by $b_{u,i}(1 + |y|^2)^N$. Put $B_{i,k} = C_k \sum_{u \in U_k} b_{u,i}$. This gives (3) and (4).

For (5), apply Fourier inversion on $K$ at $1$ to $k \mapsto f(yk)$, with the bounds (3) for $k = 0$ at $yk'$, since $|yk'| = |y|$. $\square$

### Rewriting finite sums of coefficients

**Theorem 5.8.8 (Trace bound).** Let $\mathcal{H}$ be complete and $\sigma$ standard. There are $X_1, \dots, X_d \in \mathfrak{k}$ with $|X_i| \le 1$ with this property. Let $\Delta = 1 + \Omega_X$, where $\Omega_X$ is the Casimir operator of $X$. For each finite set $S$ of words there are $r$ and $A$ such that
$$\sum_i \frac{\|e_i\|_S^2}{\mu_i^r} \le A$$
for every finite orthonormal family of $K$-finite vectors $e_i$ with $\Delta e_i = \mu_i e_i$ and $\mu_i \ge 1$.

Lean: `GlobalTheory.TypeSum.TraceBound.trace_bound`.

*Proof.* Take $X$ from orthonormal bases of the Lie algebras. The Casimir operator of $G$ acts by a scalar on smooth vectors. A Hilbert-Schmidt lemma gives words $S_0$ and $C_0$. Apply the bounded frame lemma for words on weighted eigenvectors of $\Delta$ to the words $l_0 l$ with $l_0 \in S_0$ and $l \in S$, with the elliptic estimate for $\Delta$ as input. It gives $s$ and $C$. Take $r = 2s$ and $A = |S|^2 C_0 \max(C, 0)$. $\square$

**Theorem 5.8.9 (Rewriting with a common growth exponent).** Assume the two published results. Let $\mathcal{H}$ be complete, $\sigma$ standard, and $N \in \mathbb{N}$. There are a finite set $S$ of words and maps $m$ and $A$ on finite sets of words with this property. Let $\ell_1, \dots, \ell_p$ be Sobolev functionals and $x_1, \dots, x_p$ be $K$-finite vectors. Let $B_k$ be numbers with
$$\Bigl|\sum_j \ell_j\bigl(\sigma(y) D_w x_j\bigr)\Bigr| \le B_k (1 + |y|^2)^N$$
for $y \in G$ and $|w| \le k$, with letters $X \in \mathfrak{k}$ and $|X| \le 1$. Then there are smooth vectors $x'_i$, linear forms $\ell'_i$ and $c_i \ge 0$, for $i \le q$, such that:

1. $|\ell'_i(w)| \le c_i \|w\|_S$ for smooth $w$;
2. $\sum_i c_i \|x'_i\|_{S'} \le A(S')\, B_{m(S')}$ for each finite set $S'$ of words;
3. $\sum_j \ell_j(\sigma(y) x_j) = \sum_i \ell'_i(\sigma(y) x'_i)$ for $y \in G$.

Lean: `GlobalTheory.TypeSum.CoefRep.exists_rewrite` (also `GlobalTheory.T.exists_common_growth_exponent_gK_discreteSeries`, a second name).

*Proof.* The Casselman-Wallach theorem and a lemma give $S$ and $C$ such that, if $\sum_j \ell_j(\sigma(y)x_j)$ has growth $M(1 + |y|^2)^N$, then $|\sum_j \langle e, x_j \rangle \ell_j(w)| \le C M \|e\|_S \|w\|_S$. Take $X$ from the [trace bound](/entry/trace-bound/), with exponent $r(T)$ and constant $A(T)$ for each $T$.

A lemma gives an orthonormal family of $K$-finite vectors $e_1, \dots, e_q$, with $\Delta e_i = \mu_i e_i$ and $\mu_i \ge 1$, whose span contains each $x_j$. The power $\Delta^t$ is a sum of derivatives along words of length at most $2t$ with letters from $X$, and the sum of the norms of its coefficients is at most $(1+d)^t$. So $\sum_j \ell_j(\sigma(y)\Delta^t x_j)$ has growth $(1+d)^t B_{2t}(1+|y|^2)^N$. Since $\langle e_i, \Delta^t x_j \rangle = \mu_i^t \langle e_i, x_j \rangle$, the coefficient bound gives
$$\Bigl|\sum_j \langle e_i, x_j \rangle \ell_j(w)\Bigr| \le \frac{C (1+d)^t B_{2t}\, \|e_i\|_S}{\mu_i^t}\, \|w\|_S .$$
Put $x'_i = e_i$, $\ell'_i = \sum_j \langle e_i, x_j \rangle \ell_j$, and let $c_i$ be the infimum over $t$ of the factor before $\|w\|_S$. Then (1) holds, and (3) follows from $x_j = \sum_i \langle e_i, x_j \rangle e_i$. For (2), take $t = r(S \cup S')$. Since $\|e_i\|_S \|e_i\|_{S'} \le \|e_i\|_{S \cup S'}^2$, the trace bound gives (2) with $m(S') = 2r(S \cup S')$ and $A(S') = C(1+d)^{r(S \cup S')} \max(0, A(S \cup S'))$. $\square$

### Coefficient series from $K$-types and from limits

**Theorem 5.8.10 ($K$-types give a coefficient series).** Assume the two published results. Let $\mathcal{H}$ be complete, $\sigma$ standard, and $f$ continuous on $G$ with uniform moderate growth. Assume that for each continuous $K$-finite function $e$ on $K$ there are Sobolev functionals $\ell_j$ and $K$-finite vectors $x_j$, for $j \le m$, with
$$\int_K e(k) f(yk)\, dk = \sum_j \ell_j(\sigma(y) x_j) \qquad (y \in G).$$
Then $f$ is a coefficient series of $\sigma$.

Lean: `GlobalTheory.TypeSum.KSeries.hasTypeAll_of_kTypes` (also `GlobalTheory.T.discreteSeriesCoeffSeries_of_kTypeProjections`, a second name).

*Proof.* Take $e_i$, $N$, $\Phi$ and $B$ from the [right $K$-Fourier series](/entry/exists-right-kfourier/) of $f$, and $S$, $m$ and $A$ from the [rewriting theorem](/entry/exists-rewrite/) for this $N$. For each $i$, the hypothesis applied to $e_i$ gives $\ell_{ij}$ and $x_{ij}$. The derivatives of $\sum_j \ell_{ij}(\sigma(y)x_{ij})$ are the functions $\Phi_{i,w}$, so the rewriting theorem applies with the bounds $B_{i,k}$. It gives $x'_{ij}$, $\ell'_{ij}$ and $c_{ij}$ with
$$\sum_j c_{ij}\|x'_{ij}\|_{S'} \le A(S')\, B_{i, m(S')} .$$
The right side is summable in $i$. A lemma gives the continuous bound $\beta$ for $S$. Number the pairs $(i,j)$ through a bijection $\mathbb{N} \cong \mathbb{N} \times \mathbb{N}$, padding each finite family with zero terms. The series converges for every $S'$. Its sum at $y$ is $\sum_i \int_K e_i(k) f(yk)\, dk = f(y)$. $\square$

**Theorem 5.8.11 (Limits give a coefficient series).** Assume the two published results. Let $\lambda$ be a Harish-Chandra parameter and $\sigma$ in the discrete series with parameter $\lambda$. Let $f$ be continuous on $G$ with uniform moderate growth. Assume that for each compact set $C$ and $\delta > 0$ there are Sobolev functionals $\ell_j$ and smooth vectors $v_j$, for $j \le m$, with
$$\Bigl|f(y) - \sum_j \ell_j(\sigma(y) v_j)\Bigr| < \delta \qquad (y \in C \cap G).$$
Then $f$ is a coefficient series of $\sigma$.

Lean: `GlobalTheory.ClosureSeries.hasTypeAll_of_closure` (also `GlobalTheory.T.hasAllKTypes_of_closure_discreteSeriesCoefficients` and `GlobalTheory.ClosureSeries.closure_model`, a second and a third name).

*Proof.* The space $\mathcal{H}$ is complete by definition, and a lemma that uses the structure of Harish-Chandra modules shows that $\sigma$ is standard. Apply the theorem on $K$-types. Fix a continuous $K$-finite $e$. The average $y \mapsto \int_K e(k) f(yk)\, dk$ is continuous with uniform moderate growth. The same average of the approximating sums is a sum of coefficients $\ell(\sigma(y)w)$ with $K$-finite $w$ in a fixed finite-dimensional space, and these converge to it uniformly on compact sets. A last lemma shows that such a limit is again a finite sum $\sum_j L_j(\sigma(y) w_j)$ with Sobolev functionals $L_j$. $\square$

**Remark 5.8.12 (Formalization).** The three names of the last theorem have one statement, and the name `closure_model` in [AutomorphicFormUniformLimitDiscreteSeriesSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/AutomorphicFormUniformLimitDiscreteSeriesSeries.lean#L49) names no model. In [HasAllKTypesOfClosureDiscreteSeriesCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/HasAllKTypesOfClosureDiscreteSeriesCoefficients.lean#L23) the hypothesis `IsHCParam lam` is bound to `_` at line 32 and not used; the conclusion uses `lieOf (Jm ε)` and `UH (Jm ε)`, and the proof gives `lieSet ε` and `UJset ε`, which the elaborator accepts as the same sets. In [ExistsCommonGrowthExponentGKDiscreteSeries.lean](lean:Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsCommonGrowthExponentGKDiscreteSeries.lean#L41) the hypothesis `_hHC` (line 53) is not used. The theorem on $K$-types needs only `Std`, not `IsDS`. We did not open the lemmas named in the proofs; the proofs follow their statements. We have not unfolded `SmoothVec`, `Sobolev₂`, `onePlusCas`, `lowK`, `IsSqIntOn`, `IsFdeg` or the two published inputs.

## Notes and references

The pointwise bound for discrete series coefficients is used in the step [HypsAlt is nonempty](/step/nonempty-hyps/) of [the unitary hypotheses](/proof/unitary-hypotheses/). The least value bound for theta generators is used in the step [EveryCharacter from the literature](/step/every-character-of-literature/) of [the literature](/proof/literature/). The series of the last section feed into [Theorem 3.6 of Volume 14](/entry/cuspidal-lift-smooth-at-of-cuspidal-lift/) on smooth cuspidal lifts in Volume 14.

Sections 1 to 6 follow Harish-Chandra's method: a matrix coefficient is an eigenfunction of the center of the enveloping algebra, and its radial part is bounded by a system of differential equations. Section 7 uses formal groups and Hodge-Tate characters. Section 8 uses the $K$-Fourier series and the Casselman-Wallach theory of smooth globalizations.

- Harish-Chandra, *Discrete series for semisimple Lie groups II*, Acta Math. 116 (1966), 1-111.
- N. R. Wallach, *Real Reductive Groups I*, Academic Press (1988), Ch. 3-4; *Real Reductive Groups II*, Academic Press (1992), 11.6.
- A. W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton (1986), Ch. VIII-IX.
- H. Hecht and W. Schmid, *A proof of Blattner's conjecture*, Invent. Math. 31 (1975), 129-154.
- W. Casselman and D. Miličić, *Asymptotic behavior of matrix coefficients of admissible representations*, Duke Math. J. 49 (1982), 869-930.
- S. Helgason, *Groups and Geometric Analysis*, Academic Press (1984), Ch. I §5.
- J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer GTM 9 (1972), §6.2.
- J. Tate, *p-divisible groups*, in *Proc. Conf. Local Fields (Driebergen 1966)*, Springer (1967).
- L. Fargues, *L'isomorphisme entre les tours de Lubin-Tate et de Drinfeld et applications cohomologiques*, Progr. Math. 262, Birkhäuser (2008).
