---
title: Norms of normalized theta families
decls:
  - GlobalTheory.T.normalisedFamily_normBound_absoluteConstant
  - GlobalTheory.ColNorms.FamilyBound.familyNorms
  - GlobalTheory.T.exists_thetaZeroMeanLogLeConstMul
  - GlobalTheory.Theta0MeanLeC.theta0MeanLeC
  - GlobalTheory.T.normalisedFamily_eq_tensorPower_vacuum
  - GlobalTheory.FamilyTieProof.familyTie
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Norms of normalized theta families

This section proves the two facts on normalized theta families that [the bounds on the kernel chain](/entry/ker-side-chain-s/) of section 15 uses, in step 3 of its proof. The first fact identifies each member of the family with a tensor power of the genus one vacuum, up to a constant of modulus one. The second fact bounds the mean of the log norms of the family over the embeddings of a number field, with an absolute constant. Both feed the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/).

### The setting

Let $D$ be a datum with host field $E$ and field $K$. A *curve ideal* $\mathfrak{c}$ of $K$ and a twelfth root $\delta$ of the discriminant of its lattice give a lattice $\Lambda = \Lambda(\mathfrak{c}, \delta)$ in $\mathbb{C}$. For a two torsion point $t$ of $\mathbb{C}/\Lambda$ that the even theta function does not kill, let $\theta_0(\Lambda, t)$ be the even theta function of characteristic $t$. Let $\|G\|^2_{\Lambda}$ be the genus one mean square norm of a function $G$ on $\mathbb{C}$.

A pair of lattices $L \subseteq E^N$ and $L' \subseteq E^{N'}$ is *admitted* if both are self dual and $N N'$ is even. Let $f_F$ be the degree factor of $D$. For a base $B$ of the datum, which holds a two torsion point $t_B$ and a kernel, and a character $\chi$ of ideals of $E$, the *normalized family* is a function $e_\chi(N, N', L, L')$ on the vector space $V(N, N')$ for each admitted pair. It is the theta vector of the base, multiplied by the factor

$$c_\chi(L, L') = \chi(\det L)^{z} \chi(\det L')^{z'},$$

where $\det L$ is the relative determinant ideal of $L$ against the standard lattice and $z, z'$ are integers.

A function $G$ on $V(N, N')$ is a *vacuum up to units* at $t_0$ if there are an orthonormal family $b$ of $f_F N N'$ matrices of size $N' \times N$ and a constant $\kappa$ with $|\sigma(\kappa)| = 1$ for every embedding $\sigma$, such that $G = \kappa\, I_b(\theta_0(\Lambda, t_0))$, the tensor power of the genus one vacuum along $b$.

For a number field $M \subseteq \mathbb{C}$ and points $t = (t_\rho)$ indexed by the embeddings $\rho$ of $M$, put

$$\mathrm{mlog}_M(\Lambda, t) = \frac{1}{[M : \mathbb{Q}]} \sum_{\rho} \log \bigl\|\theta_0(\rho\Lambda, t_\rho)\bigr\|^2_{\rho\Lambda}.$$

Let $\ell'(D)$ be the log derivative at $1$ of the $L$-function of the datum, and let $v$ be the size of the host. The datum has *mean bound* $C$ if, for every $(\mathfrak{c}, \delta, M, t)$ with $M$ containing the data of the torus and each $t_\rho$ an admissible two torsion point, and for every $L_{\mathrm{sc}}$ with $\log v + |\ell'(D)| \leq L_{\mathrm{sc}}$, we have $\mathrm{mlog}_M(\Lambda, t) \leq C L_{\mathrm{sc}}$.

### The family is a vacuum

**Theorem 7.16.1 (Normalized family is a vacuum).** Let $D$ be a datum with an induced CM type, $\mathfrak{c}$ a curve ideal, $\delta$ a twelfth root of the discriminant, $B$ a base with a finite kernel, and $\chi$ a character of ideals of norm one type. Then for every admissible two torsion point $t_0$ and every admitted pair $(L, L')$, the normalized family $e_\chi(N, N', L, L')$ is a vacuum up to units at $t_0$.

Lean: `GlobalTheory.T.normalisedFamily_eq_tensorPower_vacuum` (also `GlobalTheory.FamilyTieProof.familyTie`).

*Proof.* We take the steps in order.

1. The base theta vector is the vacuum at the standard lattices in even ranks: it is a vacuum up to units at the point $t_B$ of the base.
2. For two admissible two torsion points $t$ and $t'$, the theta functions $\theta_0(\Lambda, t)$ and $\theta_0(\Lambda, t')$ are equal. Indeed, the admissible point is unique up to $\Lambda$, and the even theta function is invariant under translation by $\Lambda$. So a vacuum up to units at $t_B$ is one at $t_0$.
3. Moving the vacuum from the standard lattices to $(L, L')$ keeps it a vacuum up to units at $t_0$.
4. The relative determinant ideal of a self dual lattice has norm one. A character of norm one type has modulus one at all embeddings on ideals of norm one. A product of integer powers of such values has modulus one at all embeddings. So $|\sigma(c_\chi(L, L'))| = 1$ for every $\sigma$.
5. A constant of modulus one at all embeddings times a vacuum up to units is a vacuum up to units: replace $\kappa$ by $c_\chi \kappa$.

This proves the theorem. $\square$

### The mean of the theta constants

**Theorem 7.16.2 (Mean bound for theta constants).** There is $C \geq 0$ such that every datum has mean bound $C$.

Lean: `GlobalTheory.T.exists_thetaZeroMeanLogLeConstMul` (also `GlobalTheory.Theta0MeanLeC.theta0MeanLeC`).

*Proof.* The theorem on the mean log norm of the conjugates of $\theta_0$ follows from the Weber formula for theta constants and the period formula for the eta function of a lattice. Its conclusion has several parts, and one of them is this statement. $\square$

### The norm bound

The family has *bounded norms* with constant $C$ if it has four properties at every admitted pair:

1. the norm square of $e_\chi(N, N', L, L')$ does not depend on the admitted pair, for fixed $N$ and $N'$;
2. for every number field $M$ containing the data and the coefficients, and every $L_{\mathrm{sc}} \geq \log v + |\ell'(D)|$, the mean over the embeddings $\rho$ of $M$ of $\log$ of the norm square of the conjugate family is at most $C f_F N N' L_{\mathrm{sc}}$;
3. at each embedding $\rho$ of such an $M$, the norm square of the conjugate family does not depend on the admitted pair;
4. the norm square is invariant under the translation operators $U(x)$ for $x \in V(N, N')$.

**Theorem 7.16.3 (Norm bound for normalized families).** There is a constant $C$ such that for every datum $D$ with an induced CM type, every curve ideal $\mathfrak{c}$ and root $\delta$, every base $B$ with a finite kernel and every character $\chi$ of norm one type, the normalized family has bounded norms with constant $C$.

Lean: `GlobalTheory.T.normalisedFamily_normBound_absoluteConstant` (also `GlobalTheory.ColNorms.FamilyBound.familyNorms`).

*Proof.* Let $C$ be the constant of [the mean bound for theta constants](/entry/exists-theta-zero-mean-log-le-const-mul/). Fix the data. By [the vacuum theorem](/entry/normalised-family-eq-tensor-power-vacuum/), each member of the family is a vacuum up to units at every admissible point.

1. Properties 1 and 4 come from the theta link at the base, which holds since the base is standard.
2. Let $M$ contain the data and the coefficients, and let $\rho$ be an embedding of $M$. There is an admissible two torsion point $t_\rho$ of $\rho\Lambda$. The conjugate of a vacuum up to units by $\rho$ is a vacuum for $\rho\Lambda$, and the norm square of a tensor power is a power of the genus one norm. So

$$\bigl\|e^{\rho}_\chi(N, N', L, L')\bigr\|^2 = \bigl\|\theta_0(\rho\Lambda, t_\rho)\bigr\|^{2 f_F N N'}_{\rho\Lambda}.$$

The right side does not depend on $(L, L')$. This gives property 3.
3. Take the logarithm and the mean over $\rho$. The mean of the log norm squares is $f_F N N'\, \mathrm{mlog}_M(\Lambda, t)$. The mean bound gives $\mathrm{mlog}_M(\Lambda, t) \leq C L_{\mathrm{sc}}$. Since $f_F N N' \geq 0$, the mean is at most $C f_F N N' L_{\mathrm{sc}}$. This gives property 2.

This proves the theorem. $\square$

The proof does not use $C \geq 0$. The constant enters only through the mean bound, where a factor $f_F N N' \geq 0$ multiplies it.

**Remark 7.16.4 (Formalization).** The three statements with the prefix `T.` are `first | exact` wrappers in the files named after them. The proof `familyNorms_of` in [NormalisedFamilyNormBoundAbsoluteConstant.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NormalisedFamilyNormBoundAbsoluteConstant.lean#L56) at line 56 takes the family tie and the mean bound as hypotheses, drops the condition $0 \leq C$ with a pattern `-`, and builds the four parts from `theta_link_holds`, `mean_le_of`, `conj_indep` and the theta link again; `familyNorms` then feeds it the two theorems. The norm identity is `conj_normSq`, and `genusOne_meanSquare_forms_agree` matches two definitions of the genus one norm. The four parts are the predicate `th22` at line 393 of [ColumnData.lean](lean:Formalism/LocalToGlobal/KernelLattices/ColumnData.lean#L393), the mean is `meanLog` at line 15 of [SignedLogMeans.lean](lean:Development/AbelianVarietyTheory/BlockTheory/GlobalSignature/SignedLogMeans.lean#L15) and the mean bound is `MeanLeC` at line 40 of the same file. The proof `theta0MeanLeC` in [ExistsThetaZeroMeanLogLeConstMul.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsThetaZeroMeanLogLeConstMul.lean#L10) at line 10 is the projection `.1.2.2` of a larger theorem. The vacuum proof `familyTie` is in [NormalisedFamilyEqTensorPowerVacuum.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NormalisedFamilyEqTensorPowerVacuum.lean#L71) at line 71, with the modulus lemmas `mod1All_mul'`, `mod1All_inv`, `mod1All_pow` and `mod1All_zpow`. The vacuum predicate is `ThetaVectorUpToUnits` at line 197 of [StandardLatticesGL3.lean](lean:Formalism/SharpRestriction/GlobalSchurBounds/StandardLatticesGL3.lean#L197), and the family predicates `FamilyTie` and `FamilyNorms` are at lines 80 and 88 of [CosetRefinement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CosetRefinement.lean#L80).
