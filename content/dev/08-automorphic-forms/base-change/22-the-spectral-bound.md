---
title: The spectral bound
decls:
  - UpperTheory.Zero.ConvolutionTheory.EB.specP
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The spectral bound

This section bounds the operator norm of a Hecke combination on a closed invariant subspace of an $L^2$ space on $\mathrm{GL}_a \times \mathrm{GL}_b$ by the values of the combination on finitely many cuspidal data. It is the spectral input of the trace comparison below the step [EveryCharacter](/step/every-character/): the candidates of a frame in [Section 7.16.7](/entry/block-candidates-of-inputs/) and the eigenfunctions of [Section 7.14.3](/entry/gel-of-of/) are read through it. In contrast to the previous section, the field here is a CM field.


Let $E$ be a CM field. Fix $a, b \ge 0$, dominant weights $l_1$ and $l_2$ for $\mathrm{GL}_a$ and $\mathrm{GL}_b$ at the archimedean places, and a fundamental domain datum for $(a, b)$ as in [Section 7.14.3](/entry/gel-of-of/). An archimedean datum $\mathcal{A}$ for $(l_1, l_2)$ consists of compatible measures, a bump function and archimedean kernels normalised to $1$; it determines a Hilbert space $\mathcal{H}$ of square integrable vector-valued functions on the fundamental domain, and a right convolution operator $\Phi^{\mathrm{op}}$ on $\mathcal{H}$ for each tensor kernel $\Phi$ of Section 14. We write $\chi_1$ and $\chi_2$ for the archimedean parameters of $l_1$ and $l_2$.

A cuspidal datum for $\mathrm{GL}_N$ is a list of cuspidal representations of $\mathrm{GL}_{N_i}$ with $\sum N_i = N$; its Satake parameter at $w$ is the union of the Satake parameters of its members. A predicate $P$ is a condition on a field $E$, an integer $N$, a cuspidal datum for $\mathrm{GL}_N$ and a family of multisets indexed by the complex embeddings of $E$.

**Definition 7.22.1 (Closed kept subspace, tests).** A closed subspace $Q \subset \mathcal{H}$ is kept if every operator $\Phi^{\mathrm{op}}$ of a test matrix $\Phi$ maps $Q$ into $Q$. A sequence $g = (g_k)$ in $\mathcal{H}$ tests $Q$ if each $g_k$ lies in $Q^\perp$ and every component of $g_k$ has finite weighted $L^2$ norms for all powers of the weight. Let $X$ be a set of at most one cuspidal representation of $\mathrm{GL}_a$, each invariant under the split centre. The sequence $g$ sees $X$ at level $K$ and type $W$ if every family $f$ orthogonal to all $g_k$ whose nonzero slices in the first variable are of type $(K, W)$ has no slice equal to a form of $X$ times $|\det|^z$ for some $z \in \mathbb{C}$.

For a finite set $T$ of places and exponents $e_1, e_2$, a Hecke combination $\mathcal{A}_{T, e_1, e_2}$ is a combination of tensor kernels, and for a pair of Satake families $(B_1, B_2)$ it has a value $\mathrm{val}_{T, e_1, e_2}(B_1, B_2)$, the product over $w \in T$ of local values. We say $U$ represents $\mathcal{A}_{T, e_1, e_2}$ with bound $R$ if $U = \sum_j c_j \Phi_j^{\mathrm{op}}$ for a finite combination of tensor kernels whose finite parts all equal the finite part of $\mathcal{A}_{T, e_1, e_2}$, with sizes at most $R$ and archimedean value $\sum_j c_j \Phi_j(\chi_1, \chi_2) = 1$.

Following the reading of Satake parameters in Section 15, a predicate $P$ is read on cusp forms if the following holds. For every open subgroup $K$, finite-dimensional type $W$, finite set of bad places, archimedean parameter $m_0$ and set $X$ as above, there are finitely many cuspidal data $D_j$, none containing a member of $X$, with Satake parameters $C_j$ off the bad places and with $P(D_j, m_0)$, such that every sequence of nonzero automorphic forms of type $(K, W)$, with archimedean parameters tending to $m_0$ and not twists of $X$, has a subsequence whose Satake eigenvalues converge to those of some $C_j$ at every good place.

**Theorem 7.22.2 (Spectral bound).** Let $P$ be a predicate that is read on cusp forms. Let $E$ be a CM field, $a$, $b$, $l_1$, $l_2$, a fundamental domain datum and an archimedean datum $\mathcal{A}$ as above. Let $S$ be a section, $Z$ a finite set of places in $S$ that split, $L$ a level that is maximal off $Z$, and $X$ as above. Let $Q \subset \mathcal{H}$ be closed and kept, and assume that for every finite-dimensional $W$ there is a sequence that tests $Q$ and sees $X$ at level $L_1$ and type $W$. Then there are finitely many pairs of cuspidal data $(D_{1,j}, D_{2,j})$ for $\mathrm{GL}_a$ and $\mathrm{GL}_b$, with Satake parameters $B_{1,j}$ and $B_{2,j}$ at every place off $Z$, such that no $D_{1,j}$ contains a member of $X$, $P$ holds for $(D_{1,j}, m(l_1))$ and $(D_{2,j}, m(l_2))$, and the following holds. For all $T$ disjoint from $Z$ with exponents $e_1, e_2$ adapted to $S$ and every $\rho > 0$ with
$$|\mathrm{val}_{T, e_1, e_2}(B_{1,j}, B_{2,j})| < \rho \quad \text{for all } j,$$
there are $R \ge 0$ and an operator $U$ that represents $\mathcal{A}_{T, e_1, e_2}$ with bound $R$ and satisfies $\|U|_Q\| < \rho$.

Lean: `UpperTheory.Zero.ConvolutionTheory.EB.specP`.

The proof has two steps, each an input proved elsewhere in the development.

1. (Reading.) If $P$ is read on cusp forms, then it is read on eigenvalue systems: there are finitely many pairs $(D_{1,j}, D_{2,j})$ as in the theorem such that every system of eigenvalues of the Hecke combinations that is realised by limits of eigenfunctions orthogonal to the tests, with the prescribed archimedean values, has its value at $\mathcal{A}_{T, e_1, e_2}$ equal to $\mathrm{val}_{T, e_1, e_2}(B_{1,j}, B_{2,j})$ for some $j$.
2. (Peak.) Let $t$ be a countable family of combinations whose operators are normal and commute with each other and with their adjoints, $Q$ closed and kept, and $g$ a test sequence. Assume the archimedean parameters are Hermitian, the base combination has archimedean value $1$ and a self-adjoint idempotent finite part, and every realised eigenvalue system $s$ with the prescribed archimedean values has $|s(x)| < \rho$. Then there is $V$ representing the base combination with $\|(t_x^{\mathrm{op}} \circ V)|_Q\| < \rho$.

*Proof.* By step 1, every realised eigenvalue system has value at $\mathcal{A}_{T, e_1, e_2}$ among the finitely many numbers $\mathrm{val}_{T, e_1, e_2}(B_{1,j}, B_{2,j})$, each of absolute value less than $\rho$. The operators of the Hecke combinations commute and are normal, the finite part of the base combination is a self-adjoint idempotent, and they multiply as Hecke operators. So step 2 applies and gives the operator $U$. $\square$

**Remark 7.22.3 (Formalization).** The spectral bound is the one-line term at [StableBlockG.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/EndomorphismSlices/StableBlockG.lean#L22): `rSpec_of` applied to `peakRun`, `genSt`, `ptOk`, `hkMul`, `repAlg`, `positionTest` and to `rRead P h`. The statements `CuspReadP`, `Read` and `Spec` are in [CuspReadPTrue.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/EndomorphismSlices/CuspReadPTrue.lean#L23). We did not unfold `rSpec_of`, `rRead`, `genSt`, `ptOk`, `hkMul`, `repAlg` or `positionTest`; the account of step 2 follows the statement `PeakRun` in `SphComm2.lean` (line 77), and the proof sketch above is only the way these inputs fit together.
