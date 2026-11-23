---
title: The matrix step and coupling factors
decls:
  - GlobalTheory.Core.Ht2.factors_leS
  - GlobalTheory.T.norms_matrixSteps_coupledFactor_bounded_anyLevelPrime
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The matrix step and coupling factors

This section bounds the growth of norms along a kernel chain at one complex place. Each matrix step and the final coupling multiply the square norm by at most the exponential of an explicit sum of log periods, a log theta value, counts and one error term. The constant in the error term is uniform, and the level is any prime. The result is used in [the kernel side of the chain bound](/entry/ker-side-chain-s/), also stated as [the kernel half of the chain numbers at any prime level](/entry/kernel-half-chain-numbers-any-level-prime/). Its inputs include [the family tie](/entry/family-tie/), which holds by [the tensor power form of the normalised family](/entry/normalised-family-eq-tensor-power-vacuum/).

**Setting.** A *kernel chain* $Q$ over a number field $K$ has families $F_0, \dots, F_n$ of forms, a last space $S_1$, linear steps $\mathrm{st}_i \colon F_i \to F_{i+1}$ for $i < n$, and a coupling $\mathrm{cp} \colon F_n \to S_1$. The family $F_i$ has a finite index set $\beta_i$ of members. Each member $b$ has a finite set $\mathrm{Cl}(b)$ of classes and a hermitian form $\langle \cdot, \cdot \rangle_{b,v}$ at each infinite place $v$ of $K$. For $\varphi \in F_i$ put
$$\|\varphi\|_v^2 = \operatorname{Re} \sum_{b \in \beta_i} \langle \varphi_b, \varphi_b \rangle_{b,v}.$$
The step $i$ has the *square bound* with exponent $t$ at $v$ if $\|\mathrm{st}_i \varphi\|_v^2 \leq e^t \|\varphi\|_v^2$ for all $\varphi \in F_i$. The coupling has the square bound with exponent $t$ if $\|\mathrm{cp}\, \varphi\|_{S_1,v}^2 \leq e^t \|\varphi\|_v^2$ for all $\varphi \in F_n$.

A numerical datum gives a degree $f$, a number $m$ of steps, sizes $N_j$ with maximum $N_{\max}$, conductors $g_0, g_1$, a constant $c_N$, and for a code $\delta$ rational exponents $\nu_{j,z,i}$ at the places $z$ of the row set $R$. Put $|\nu|_{j,z} = \sum_{i < N_{j-1}} \nu_{j,z,i}$ and $\phi(y) = y \log y - y$. For a prime $T$ the *error unit* is $U = f m^2 N_{\max}^2 \log(g_0 g_1 T)$. For $C \in \mathbb{R}$, log periods $\ell\Omega_z$, a log theta value $\ell\Theta$ and natural numbers $h, h', n, n'$, the *kernel exponent* of step $j$ is
$$\begin{aligned}
\kappa_j(C; h, h', n, n') ={}& \sum_{z \in R} \Big( \sum_{i < N_{j-1}} \phi(\nu_{j,z,i}) - |\nu|_{j,z}\, \ell\Omega_z \Big) + \ell\Theta \\
&+ f N_{j-1} N_j \log\big(8 + 32 f N_{j-1} N_j c_N\big) + 2 C U \\
&+ \sum_{z \in R} \Big( 1 + 2 N_{j-1} N_j \log\big(2 |\nu|_{j,z} + 2\big) \Big) + \log(h h') + \log(n n').
\end{aligned}$$
The *lift exponent* $\lambda_j(C)$ is $\kappa_j$ with $T = T_u$ the prime of the word $u$, $\ell\Omega_z$ the log period at the place of $z$ read through an embedding $\rho$, $\ell\Theta$ the log theta value of the sizes $N_{j-1}, N_j$, $h = h_{j-1}$ and $h' = h_j$ the class numbers of the steps, and $n = n_{j-1}$ and $n' = n_j$ the index counts of the steps.

We use six inputs, each a statement proved elsewhere in the volume:

1. the block bound for padded Witt norm squares;
2. the family tie;
3. nonzero theta vectors of the normalised family over a number field;
4. the period lattice properties of the normalised family;
5. the coset indicator refinement of theta vectors;
6. the mean of log periods, from the Chowla-Selberg formula.

**Theorem 2.28.1 (Matrix step and coupling factors).** Assume inputs 1 to 6. Then there is $C_K \geq 0$ with the following property. Take any constant $C_Y$ and any tower data, fields, primes, weights, characters and selections that satisfy the chain hypothesis for $C_Y$. Take any base $B$ with a field of definition, any intermediate field $\mathbb{Q} \subseteq M \subseteq \mathbb{C}$ of finite degree with theta field data, and any embedding $\rho \colon M \to \mathbb{C}$. Let $Q$ be the kernel chain of the columns, with $n = m - 2$, and let $v$ be the infinite place of $K$ under $\rho$. Then:

1. for every $i$ with $i + 2 < m$, the step $i$ of $Q$ has the square bound with exponent $\lambda_{i+1}(C_K)$ at $v$;
2. the coupling of $Q$ has the square bound with exponent $\lambda_{m-1}(C_K) + \lambda_m(C_K)$ at $v$.

Lean: `GlobalTheory.Core.Ht2.factors_leS` (also `GlobalTheory.T.norms_matrixSteps_coupledFactor_bounded_anyLevelPrime`, a second name).

The constant $C_K$ is chosen before $C_Y$, so it does not depend on the chain hypothesis. The constant also appears inside the lift exponent, as the coefficient of $U$.

*Proof.* We bound the kernel entries, count the sums, and apply Cauchy-Schwarz.

1. *Finite data.* There is $C_d$ such that the finite data of the matrix entries are bounded with level size $(g_0 g_1)^{C_d f m^2 N_{\max}^2}$.
2. *Kernel entries.* From inputs 1 to 6 and $C_d$ we get $C_1 \geq 0$ such that every kernel entry between classes of steps $j - 1$ and $j$ is bounded at $v$, as an operator, by $e^{k_j}$, where $k_j = \kappa_j(C_1; 1, 1, 1, 1)$ with the data of $\lambda_j$.
3. *Class numbers.* There is $C_c \geq 0$ such that the class sets of each step, of the evaluation datum and of the top have at most $e^{C_c U}$ elements.
4. *Indices.* There is $C_i \geq 0$ with $|\beta_j| \leq e^{C_i U}$ for every step $j$.
5. *Cosets.* There is $C_y \geq 0$ such that the coupling coset sets have at most $e^{C_y U}$ elements.
6. *Choice of constant.* Put $C_K = C_1 + C_c + C_i + C_y$. Since $\log x \geq 0$ for every natural number $x$,
$$k_j + 2 (C_c + C_i + C_y) U \leq \lambda_j(C_K).$$
Since $T_u$ is prime and $g_0, g_1 \geq 1$, also $U \geq 0$.
7. *Positivity.* The coefficient Gram matrices are positive semidefinite at $v$. So the hermitian forms of all members are positive at $v$, and $\|\varphi\|_v^2 \geq 0$.
8. *Steps.* Fix $i$ with $i + 2 < m$. The Cauchy-Schwarz bound for class sum matrices gives
$$\|\mathrm{st}_i \varphi\|_v^2 \leq |\beta_i|\, |\beta_{i+1}|\, h\, h'\, e^{k_{i+1}}\, \|\varphi\|_v^2,$$
where $h$ and $h'$ bound the class sets of the members of $F_i$ and $F_{i+1}$. By steps 3 and 4 the factor is at most $e^{2 C_i U + 2 C_c U + k_{i+1}}$, and by step 6 this is at most $e^{\lambda_{i+1}(C_K)}$.
9. *Coupling.* The coupled Cauchy-Schwarz bound uses the first coupled kernel and the last kernel. Their finite data have level sizes that step 1 bounds; the bounds are weakened with $(g_0 g_1)^{e} \geq 1$ for $e \geq 0$. With steps 3, 4 and 5 the factor is at most $e^{C_i U + 4 C_c U + 2 C_y U + k_{m-1} + k_m}$. By step 6 this is at most $e^{\lambda_{m-1}(C_K) + \lambda_m(C_K)}$. $\square$

The class numbers and index counts enter the lift exponent only through $\log(h h')$ and $\log(n n')$. The proof does not use their size there. It uses only that these logs are nonnegative, and it absorbs the true counts into $C_K U$.

**Remark 2.28.2 (Formalization).** The theorem is at [NormsMatrixStepsCoupledFactorBoundedAnyLevelPrim.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/NormsMatrixStepsCoupledFactorBoundedAnyLevelPrim.lean#L20). Its second name is in [NormsMatrixStepsCoupledFactorBoundedAnyLevelPrimStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/NormsMatrixStepsCoupledFactorBoundedAnyLevelPrimStatement.lean#L8), by a `first | exact` block under one million heartbeats. The square bounds and the lift exponent are in [TopPlaceLogTheta.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/TopPlaceLogTheta.lean#L17), at lines 17, 101, 105 and 174. Kernel chains and the family inner product are in [DivisionHeightBoundStatement.lean](lean:Formalism/LocalToGlobal/Divisibility/DivisionHeightBoundStatement.lean#L245), at lines 245 and 248. The six inputs are hypotheses of the theorem. They are defined in [PaddedWittNormSquare.lean](lean:Development/AbelianVarietyTheory/BlockTheory/DivisorBase/PaddedWittNormSquare.lean#L36), in [CosetRefinement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CosetRefinement.lean#L80) at lines 80, 84, 92 and 98, and in [MeanPeriodLogarithms.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/MeanPeriodLogarithms.lean#L15). The user discharges all six at [KernelHalfChainNumbersAnyLevelPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KernelHalfChainNumbersAnyLevelPrime.lean#L221), lines 221 to 222. The error unit is at line 70 of the coset file. The comparison of step 6 is in [ColumnNormsOf.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ColumnNormsOf.lean#L39); it uses only the nonnegativity of the two logs (lines 40 to 41). The class number bound, with constant $55$, is in [CardOrbitsLeExp.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/CardOrbitsLeExp.lean#L82), and the coset bound, with constant $2$, is in [NcardYbSetLe.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/NcardYbSetLe.lean#L10). The sum $|\nu|_{j,z}$ is named as an absolute value, but it is the signed sum of the exponents ([Numbers.lean](lean:Formalism/LocalToGlobal/Divisibility/Numbers.lean#L227)). If it is less than $-1$, the logarithm in the kernel exponent is that of a negative number, which the real logarithm reads as the logarithm of its absolute value. We have read the statements, not the proofs, of the cited bounds of steps 1 to 5 and 7 to 9.

## Notes and references

This chapter supplies the doubling and scalar inputs of the assembly volume. Section 1 gives good models of CM elliptic curves and height two at inert primes. Sections 2 to 7 give the local doubling at twist places, the Hecke parameters, the step scalars and the injectivity of the total up map; they feed [membership and bundles at the stronger parameters](/entry/member-bundles-large-unramified-exponents-alt/). Sections 8 to 18 give the see-saw laws at split and twist places, the cell sums and the finite integral laws; they feed [place laws for a rescaled tuple](/entry/laws-resc-alt/), [the column data of a true geometric family](/entry/laws-links-of-geo-rows-cols-alt/), [the column side of a geometric family](/entry/col-side-alt/) and [good extensions at a bad place](/entry/exists-quadratic-extension-reads-low/). Sections 19 to 28 give the kernel class data and their uses; they feed [the class pin of a true column](/entry/cls-pin-d-of-fam-col-of-true-w/), [commuting links from the laws](/entry/link-comm-of-laws-alt/), [matches that differ by a central element](/entry/matches-differ-central-alt/), [the shape integral in normal frames](/entry/exists-shape-integral-in-normal-frames-alt/), [the family of all levels](/entry/fam-all-q-of-all-true-alt/), [the row bound of the star term](/entry/global-theory-mi-star-row-alt-alt/), [the mean of the theta null norms](/entry/theta0-mean-le-c/) and [the kernel side of the chain bound](/entry/ker-side-chain-s/). Background is in [the Weil representation](/learn/theta/#the-weil-representation), [see-saw pairs](/learn/theta/#seesaw-pairs), [the Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula), [the doubling method](/learn/theta/#the-doubling-method), [the Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula), [the mass formula for unitary groups](/learn/hermitian-lattices/#the-mass-formula-for-unitary-groups) and [the Chowla-Selberg formula](/learn/elliptic-curves/#the-chowla-selberg-formula).

Several statements are special cases of classical results. The Siegel-Weil statement of section 26 is the coefficient form, at one index $T$, of the identity of Weil and of Kudla and Rallis between a theta integral and a Siegel Eisenstein series, in the convergent range only. The step scalars and the doubling integrals of sections 2 to 7 and 23 are cases of the doubling method of Piatetski-Shapiro and Rallis and of the Rallis inner product formula. The normalisation of section 26 by the volumes over the dimension of the representation is Schur orthogonality for a compact group. The mean of section 27 is the class mean in the Kronecker limit formula and the Chowla-Selberg formula. Its bound has the shape of the constant in that formula, written with $L'/L(1,\chi)$. The theta null identities used there are Jacobi's product formula $\theta_{00}\theta_{01}\theta_{10} = 2\eta^3$ and Weber's relations between theta nulls, $\eta$ and the Weber functions. The bounds of this section are Cauchy-Schwarz for finite matrices of operators.

- A. Weil, "Sur certains groupes d'opérateurs unitaires", *Acta Math.* 111 (1964), 143 to 211.
- A. Weil, "Sur la formule de Siegel dans la théorie des groupes classiques", *Acta Math.* 113 (1965), 1 to 87.
- C. L. Siegel, "Über die analytische Theorie der quadratischen Formen", *Ann. of Math.* 36 (1935), 527 to 606.
- R. Howe, "θ-series and invariant theory", *Proc. Sympos. Pure Math.* 33, Part 1 (1979), 275 to 285.
- S. Kudla, "Seesaw dual reductive pairs", *Progr. Math.* 46 (1984), 244 to 268.
- S. Rallis, "Injectivity properties of liftings associated to Weil representations", *Compositio Math.* 52 (1984), 139 to 169.
- S. Gelbart, I. Piatetski-Shapiro and S. Rallis, *Explicit Constructions of Automorphic L-Functions*, Lecture Notes in Math. 1254, Part A.
- S. Kudla and S. Rallis, "On the Weil-Siegel formula", *J. Reine Angew. Math.* 387 (1988), 1 to 68.
- S. Kudla and S. Rallis, "A regularized Siegel-Weil formula: the first term identity", *Ann. of Math.* 140 (1994), 1 to 80.
- A. Ichino, "A regularized Siegel-Weil formula for unitary groups", *Math. Z.* 247 (2004), 241 to 277.
- S. Chowla and A. Selberg, "On Epstein's zeta-function", *J. Reine Angew. Math.* 227 (1967), 86 to 110.
- C. L. Siegel, *Advanced Analytic Number Theory*, Chapter I.
- D. Mumford, *Tata Lectures on Theta I*, Chapter I.
- J.-P. Serre and J. Tate, "Good reduction of abelian varieties", *Ann. of Math.* 88 (1968), 492 to 517.
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, Chapters V and VII.
- J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, Chapter II.
- J. Tate, "Global class field theory", in J. W. S. Cassels and A. Fröhlich, *Algebraic Number Theory*, Chapter VII.
- G. B. Folland, *A Course in Abstract Harmonic Analysis*, Chapter 5.
