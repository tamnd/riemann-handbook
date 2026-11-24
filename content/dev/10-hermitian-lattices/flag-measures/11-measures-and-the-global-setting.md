---
title: Measures and the global setting
decls:
  - GlobalTheory.LocalStabiliserTie.exists_tied_haar
  - GlobalTheory.T.exists_frameStabilizerHaar_normalised_fibreMeasure
  - GlobalTheory.St.Rescale.rescaleStep3
  - GlobalTheory.fullExists_of_locTied
  - GlobalTheory.St.SpectralData.exists_setting
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Measures and the global setting

This section builds the measures of a Hida setting and then the global setting of a datum: a Hida setting with tied measures, a standard additive character and transports to the given forms. The local step ties a Haar measure on the stabilizer of a frame to a Haar measure on the unitary group, with the self-dual measures of the fifth section. The global step rescales the measures of a Hida setting so that they are normalised and compatible with the mass data. The global setting is step 1 of [the spectral data for large gaps](/entry/exists-spectral-data-gap-alt/), which feeds the off-diagonal bound of the ninth section through the choice of spectral ties.

### The local tie of measures

Let $E/F$ be a CM extension with conjugation $\sigma$, and let $J$ be a nondegenerate hermitian matrix of size $n$. Let $\psi$ be a standard character of $\mathbb A_F$: continuous, of norm $1$, trivial on $F$, nontrivial, with $\psi_\infty(x) = \exp(2\pi i \sum_w \operatorname{Re} x_w)$. Fix a finite place $v$ of $F$ and a standard frame $P$ of $r+1$ vectors with Gram matrix $T_P$. Write $G_v = U(J)(F_v)$, $S_v \subset G_v$ for the stabilizer of the frame as a set and $S_{0,v} \subset S_v$ for its pointwise fixer.

Say that Haar measures $\mu_G$ on $G_v$ and $\mu_S$ on $S_v$ are *tied* if there is a Haar measure $\mu_{S_0}$ on $S_{0,v}$ with two properties:

1. $\mu_G$, $\mu_{S_0}$ and the fibre measure $\omega_{T_P}$ at the Gram matrix $T_P$ are compatible: integration over $G_v$ is integration over the fibre of frames with Gram matrix $T_P$ against $\omega_{T_P}$, followed by integration over $S_{0,v}$;
2. $\mu_S$ is the product of $\mu_{S_0}$ and the self-dual measure for $\psi_v$ on the unitary group $U_{r+1}$ that permutes the frame.

**Theorem 3.11.1 (Tied Haar measure).** Assume the Siegel-Weil condition at the pair $(E/F, J)$ and the Siegel density formula for the stabilizer. Let $\psi$ be a standard character and $P$ a standard frame of $r+1$ vectors with $2(r+1) < n$. Then for each Haar measure $\mu_G$ on $G_v$ there is a Haar measure $\mu_S$ on $S_v$ tied to $\mu_G$.

Lean: `GlobalTheory.LocalStabiliserTie.exists_tied_haar` (also `GlobalTheory.T.exists_frameStabilizerHaar_normalised_fibreMeasure`, a second name).

*Proof.*

1. The Gram matrix $T_P$ of the standard frame is hermitian and invertible.
2. The two assumptions give the local self-dual measures $dX$ on frames and $dT$ on hermitian matrices of size $r+1$, and a fibre family $\omega$ for the Gram map. This needs $r + 1 \le n$ and $2(r+1) < n$.
3. There is a Haar measure $\mu_0$ on $S_{0,v}$ compatible with $\mu_G$ and the fibre family. Conjugation by a similitude preserves the Haar measure of the unitary group, so $\mu_0$ does not depend on the choice of a point in the fibre.
4. The local component $\psi_v$ is nontrivial, because $\psi$ is standard and $F$ is totally real. So there is a self-dual trace measure on the unitary group $U_{r+1}$, and it is a Haar measure.
5. $S_v$ is the product of $S_{0,v}$ and a section of $U_{r+1}$. The product of $\mu_0$ and the self-dual measure is a Haar measure $\mu_S$ on $S_v$.
6. The fibre measure at the frame is the member $\omega_{T_P}$ of the family. With step 3 this gives property 1, and step 5 gives property 2. $\square$

### The rescaled measures

A Hida setting $X$ for a datum $D$ carries a measure package: a Haar measure on $G(\mathbb A)$ with local components $\mu_{G,v}$, measures $\mu_B$ on the stabilizers of tuples, and for each word $u$ measures on the unipotent radical $N$, the frame stabilizer $H$ and the local stabilizers. The package is *normalised* if each measure is a Haar measure and the archimedean parts are the standard ones. $X$ has *tied measures* for a bridge isomorphism $h_b$ to the matrix group if the measures of $X$ are the images under $h_b$ of the product Haar measure on $G_\infty \times G_f$ and of the measures on the unipotent and stabilizer groups.

**Theorem 3.11.2 (Rescaling of measures).** Assume the Siegel-Weil formula in its convergent range. Let $X$ be a Hida setting for $D$ with tied measures for $h_b$. Then there are a normalised group package and a normalised word package $W(u)$ for each word $u$, and a standard character $\psi$, such that the setting $X'$ with these measures has these properties:

1. $X'$ has tied measures for $h_b$;
2. the stabilizer measures are compatible with $\psi$ and with the mass data;
3. at each finite place $v$ and each word $u$, the measure of $X'$ on the local stabilizer is tied to $\mu_{G,v}$.

Lean: `GlobalTheory.St.Rescale.rescaleStep3`.

*Proof.*

1. The instance of $X$ is a CM extension with an invertible hermitian matrix, and each word has a standard frame of $r_S + 1 + r_S$ vectors.
2. The Siegel-Weil formula in its convergent range gives the two volume facts at $(E/F, J)$: the Siegel-Weil condition and the Siegel density formula. A standard character $\psi$ exists because $F$ is totally real.
3. For each tuple $X_0$ of $2r_S + 2$ vectors with invertible Gram matrix, there is an adelic torus measure $\nu$ and a Haar measure $\mu'$ on the stabilizer of $X_0$, compatible with $\mu_G$. Replace $\mu_B(X_0)$ by $\mu'$. For a singular Gram matrix, keep $\mu_B(X_0)$.
4. For each word $u$, step 3 at the frame of $u$ gives the measure $\mu_H$ on the frame stabilizer. There is a Haar measure $\mu_N$ on the unipotent radical with covolume $1$. The tied Haar measure gives a local stabilizer measure $\mu_{S,v}$ at each finite place $v$.
5. There is a normalised word package $W(u)$ with these components. Its archimedean measures on $N$ and $H$ are those of $X$.
6. The archimedean parts do not change, so $X'$ keeps the tied measures. Steps 3 and 4 give property 2, and step 4 gives property 3. $\square$

### The full datum

A *full datum* for a Hida setting $X$ adds to $X$ a level character, a typed reduction, the row representatives and column systems for each word, fundamental domains at the real places, and local models with agreement at each split place. A datum $D$ has *local ties* if, at each split place $p$, the local data of $D$ are isomorphic to the local completion of $D$ at $p$.

**Theorem 3.11.3 (Full datum).** If $D$ has local ties, then each Hida setting for $D$ has a full datum.

Lean: `GlobalTheory.fullExists_of_locTied`.

*Proof.* The level set of each Hida setting is a subgroup with a unitary character. A typed reduction exists, the lattice steps hold and the local duals agree. With the local ties, the existence of a full datum from these four facts gives the result. $\square$

### The global setting

**Theorem 3.11.4 (Global setting).** Assume the Siegel-Weil formula in its convergent range. Let $D$ be a datum with a form $F(u)$ for each word $u$, and assume the gap condition: $r \ge 1801$, and consecutive Harish-Chandra parameters at each real place differ by at least $16 r^{19}$. Then there are a Hida setting $X$, a bridge isomorphism $h_b$ and a character $\psi$ of $\mathbb A_F$ such that:

1. the instance of $X$ is the instance built from the fields of $D$, and the map of CM fields in $X$ is the identity;
2. $X$ has tied measures for $h_b$;
3. $\psi$ is a standard character;
4. $\psi$ is compatible with the mass data and with the local volumes at each place;
5. if $X$ has a level character, then for each word $u$ there is a transport of $X$ to $F(u)$ that matches the level.

Lean: `GlobalTheory.St.SpectralData.exists_setting`.

*Proof.*

1. Two facts on discrete series hold: the Bessel bound for large gaps and the weighted local coefficient bound.
2. The fields of $D$ give an instance. The form $F(u_0)$ gives a lattice.
3. The additive character data, a reference frame, the adelic vectors, the automorphic bundle, the representation data and the blocks of measures exist. Only the bundle uses the gap condition.
4. The real place functions exist by step 1 and the gap condition. The last block and the bridge $h_b$ follow. This gives a Hida setting with tied measures.
5. The rescaling of measures gives the new measures, $\psi$ and properties 2 to 4. This is the only use of the Siegel-Weil formula.
6. Property 1 holds by construction. The transport theorem of the tenth section, with the identity isomorphism of adele rings, gives property 5. $\square$

The rescaling changes only the stabilizer measures $\mu_B$ and the word packages. The group measure $\mu_G$ and the bridge $h_b$ stay the same, so the volume step of the fifth section applies to $X'$ with the same constants.

**Remark 3.11.5 (Formalization).** The tied Haar measure is in ExistsFrameStabilizerHaarNormalisedFibreMeasure.lean, line 17, and the tie is `LocTieW` (LocVol.lean, line 273). The two volume hypotheses are `SWa1`, in a namespace named `UnusedSlot34`, and `StabilizerFirstChernCompatibility` (SiegelWeilNarrowOfWide.lean, line 22). The name of the second does not describe its content: it is the Siegel density formula for the stabilizer. The statement `RescaleStep3` is in LevelMatchIff.lean, line 91, and its proof is in RescaleStep3.lean, line 22. The Siegel-Weil hypothesis is `SiegelWeilUnitaryConvergent` (SiegelWeilUnitaryConvergent.lean, line 46), used through `siegelWeil_volumes`. The full datum is in FullExistsOfLocTied.lean, line 10. It is one application of `fullExists_tied` (FullTied.lean, line 43), with `level_subgroup_is_group X` as the level character. So every Hida setting has a level character, and the hypothesis of property 5 of the global setting always holds. The structure `Full` is in PoincareConstantEq.lean, line 25. `LocTied` has two identical definitions, in LocalDiscriminantIsUnit.lean, line 1734, and LocalAdditiveCharContinuous.lean, line 239. The global setting is in ExistsGlobalSetting.lean, line 45. Property 1 holds by `rfl` and `HEq.rfl` (line 68), and the adele ring isomorphism of the transport is `RingEquiv.refl` (line 69). `CoefWeightedLoc_holds` is the `Fact.out` of an instance, proved elsewhere.
