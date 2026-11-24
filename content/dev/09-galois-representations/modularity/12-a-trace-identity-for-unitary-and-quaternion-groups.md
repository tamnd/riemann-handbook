---
title: A trace identity for unitary and quaternion groups
decls:
  - UpperTheory.V.Z.Sym.Loc.kappa
  - UpperTheory.V.Z.Sym.Glob.basePt
  - UpperTheory.V.Z.Sym.Glob.embEx
  - UpperTheory.V.Z.Sym.Glob.sideG
  - UpperTheory.V.Z.Sym.Glob.tFId0
  - UpperTheory.V.Z.Sym.Sig.sigMain
  - UpperTheory.V.Z.Sym.So.datOk
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A trace identity for unitary and quaternion groups

The three-dimensional unitary automorphy of the next sections needs a transfer of automorphic forms from $U(2)$ to $U(3)$. Over the totally real subfield, $U(2)$ is close to the norm one group of a quaternion algebra. The transfer comes from a comparison of trace formulas: the trace of a twisted Hecke operator on a definite $U(3)$ is a positive multiple of a sum of traces on the quaternion norm one group, plus a multiple of a trace on the full quaternion group. This section proves that identity. Its local input is a computation of orbit counts with Hilbert symbols, and its global input is Hilbert reciprocity.

Throughout, $F$ is a totally real number field, $\Delta \in F$ is totally negative, and $E = F(\sqrt{\Delta})$. Let $U_3$ be the unitary group of the identity hermitian form in three variables for $E/F$, with its involution $\theta$. Let $D^\times$ be the group of matrices $\begin{pmatrix} a & b \\ -\bar b & \bar a \end{pmatrix}$ with $a, b \in E$ and nonzero determinant, and $D^1$ its subgroup of determinant 1.

**Definition 8.12.1 (Norm symbol).** Let $K$ be a field of characteristic not 2 and $\delta, x \in K^\times$. Put $(\delta, x)_K = 1$ if $x$ is a norm from $K(\sqrt{\delta})$, that is $x = a^2 - \delta b^2$ for some $a, b \in K$, and $(\delta, x)_K = -1$ otherwise.

For a local field $K$ this is the Hilbert symbol. The product formula $\prod_v (\delta, x)_v = 1$ over all places of $F$ is Hilbert reciprocity (J. Neukirch, *Algebraic number theory*, Chapter VI, Theorem 8.1). The statement that $x$ is a global norm when it is a local norm at every place is the Hasse norm theorem for cyclic extensions (same source, Chapter VI, Corollary 4.5).

**Definition 8.12.2 (Transfer data).** Transfer data for $\Delta$ are a nonempty finite set $\Sigma$ of finite places of $F$ at which $\Delta$ is a square, local levels at the places of $\Sigma$, and a character $\chi_v$ of $F_v^\times$ at each place. They are valid if $F$ is totally real, $\Delta$ is totally negative, $E/F$ is unramified at the finite places outside $\Sigma$, and the characters are unramified. The cone is the set of tuples $t = (t_v)_{v \in \Sigma}$ with $|t_v| < |\varpi_v|^2$.

For $\tau \in F$ and a place $v \notin \Sigma$, there are two local numbers: an orbit count $\kappa_v(c, d, m)$, which counts lattice classes attached to data $(c, d, m)$ with trace $\tau$, and an orbital integral $g_v(\tau)$ of the unit of the spherical Hecke algebra twisted by $\chi_v$. We do not need their definitions, only the identity that relates them.

**Proposition 8.12.3 (Local orbit count).** Let $v$ be a finite place of $F$ off $\Sigma$, with valuation ring $\mathcal{O}$, at which 2 is a unit and $E/F$ is unramified. Let $\tau \in F_v$ with $\tau^2 \ne 4$, and let $c \in F_v^\times$ with $c(2 - \tau)$ of even valuation. Let $\lambda \in F_v(\sqrt{\Delta})$ have norm $2 + \tau$, and put $X = 2 + \tau + \operatorname{tr} \lambda \ne 0$. Let $d_\lambda$ be the datum built from $\lambda$. Then
$$\kappa_v(c, d_\lambda, 1) = (\tau^2 - 4, X)_v\,(\Delta, X)_v\,(\tau^2 - 4, -c)_v\; g_v(\tau).$$

Lean: `UpperTheory.V.Z.Sym.Loc.kappa`.

*Proof.* If $\tau \notin \mathcal{O}$, both sides are zero: no lattice of the required kind has trace $\tau$, and the orbital integral vanishes. Let $\tau \in \mathcal{O}$. A change of $\lambda$ to another element $\lambda'$ of the same norm multiplies the left side by the product of the first two symbols for $\lambda$ and $\lambda'$. So it is enough to prove the identity for one convenient $\lambda$. The count $\kappa_v$ is a sum over $t \in F_v^\times$ of counts that depend only on the symbol $(\tau^2 - 4, t)_v$, so it is a shifted sum. We compute it in three cases, by the reduction of $\tau$ modulo $\varpi$: $2 + \tau$ a unit square, $2 - \tau$ a unit square, or neither. In each case we compare with the values of $g_v(\tau)$. $\square$

**Proposition 8.12.4 (Base points).** Let the transfer data be valid, and put $e = (-1)^{[F:\mathbb{Q}]}$. Let $\tau \in F$ with $\tau^2 - 4$ totally negative, a square at each $v \in \Sigma$, and integral off $\Sigma$. Then there is a datum $(d, m)$ of trace $\tau$ such that for each totally positive $c$ with $c(2 - \tau)$ of even valuation off $\Sigma$,
$$\prod_{v \notin \Sigma} \kappa_v(c, d, m) = e \prod_{v \notin \Sigma} g_v(\tau).$$

Lean: `UpperTheory.V.Z.Sym.Glob.basePt`.

*Proof.* Suppose first that $2 + \tau$ is a norm from $E$. Choose $\lambda$ with norm $2 + \tau$. If $2 + \tau + \operatorname{tr} \lambda = 0$, replace $\lambda$ by $-\lambda$; both cannot vanish, since $\tau \ne -2$. Take $d = d_\lambda$ and $m = 1$. The local proposition gives each factor $\kappa_v$ as three symbols times $g_v(\tau)$. At $v \in \Sigma$ the three symbols are 1, because $\tau^2 - 4$ and $\Delta$ are squares there. So by reciprocity the product of the symbols over $v \notin \Sigma$ is their product over the real places. At a real place, $\tau^2 - 4 < 0$, $\Delta < 0$, $-c < 0$ and $X > 0$, so the three symbols give $1 \cdot 1 \cdot (-1) = -1$. The product is $e$.

Suppose now that $2 + \tau$ is not a norm from $E$. At a real place $2 + \tau > 0$, so it is a norm there. At $v \in \Sigma$ it is a norm, as $\Delta$ is a square. By the Hasse norm theorem there is a place $v \notin \Sigma$ where $2 + \tau$ is not a local norm. Take any valid datum $(d, m)$. At this $v$ both $\kappa_v$ and $g_v(\tau)$ vanish, so both sides are 0. $\square$

**Proposition 8.12.5 (Elements of given trace).** Let the transfer data be valid and $\tau \in F$. If $\tau^2 - 4$ is totally negative, there is $\gamma \in D^1(F)$ with $\operatorname{tr} \gamma = \tau$. If $\gamma \in D^1(F)$ has trace $\tau$ and $\tau^2 \ne 4$, then $\tau^2 - 4$ is totally negative.

Lean: `UpperTheory.V.Z.Sym.Glob.embEx`.

*Proof.* Let $d = \tau^2 - 4$. The element $-1$ is a local norm from $F_v(\sqrt{\Delta})$ at every finite place: at $v \in \Sigma$ because $\Delta$ is a square, and elsewhere because a unit is a norm from an unramified extension. A global norm argument then gives $p_0, p_1, q_0, q_1 \in F$ with
$$\begin{aligned} p_0^2 + d p_1^2 - \Delta(q_0^2 + d q_1^2) &= -1, \\ p_0 p_1 &= \Delta q_0 q_1. \end{aligned}$$
Put $A = p_1^2 - \Delta q_1^2$, which is not zero by positivity at a real place. Then $a = \tau/2 + \sqrt{\Delta}\,(p_0 q_1 - q_0 p_1)/(2A)$ and $b = (p_1 + \sqrt{\Delta}\, q_1)/(2A)$ satisfy $a\bar a + b \bar b = 1$, and the matrix of $(a, b)$ lies in $D^1(F)$ with trace $\tau$. For the converse, write $\gamma$ with entries $a, b$. At a real place, $a \bar a + b \bar b = 1$ and $\Delta < 0$ give $(\tau/2)^2 \le 1$. As $\tau^2 \ne 4$, the inequality is strict. $\square$

Let $f_G^t$, $f_S^t$ and $f_K^t$ be the test functions on $U_3$, $D^1$ and $D^\times$ given by $t$ at $\Sigma$ and by the unit of the spherical Hecke algebra elsewhere. For a finite adele $x$ of $D^\times$, put $f_S^{t,x}(g) = f_S^t(x^{-1} g x)$. Let $B_G$, $B_S$ and $B_K$ be spaces of automorphic forms on the three groups with finite dimensional weights $W$, at the levels of the data, whose weights share one trace function $c$ on $F$: the trace of $W$ at an element of invariant $\tau$ is $c(\tau)$. Put
$$\Sigma_S(t) = \sum_\tau c(\tau)\, m(\tau)\, n_S(\tau), \qquad \Sigma_K(t) = \sum_\tau c(\tau)\, m(\tau)\, n_K(\tau),$$
where $\tau$ runs over the elements with $\tau^2 - 4$ totally negative that meet the local condition at $\Sigma$, $m(\tau)$ is a mass, and $n_S$, $n_K$ are products of orbit counts off $\Sigma$.

**Proposition 8.12.6 (The unitary side).** Let the transfer data be valid. There is $c_G > 0$ such that for each $t$ in the cone
$$\operatorname{tr}\bigl(R_\theta(f_G^t) \mid B_G\bigr) = c_G\bigl(\Sigma_S(t) + e\,\Sigma_K(t)\bigr), \qquad e = (-1)^{[F:\mathbb{Q}]}.$$

Lean: `UpperTheory.V.Z.Sym.Glob.sideG`.

*Proof.* The space $B_G$ is finite dimensional, so the twisted trace is a finite sum of orbital terms over a set of representatives of twisted conjugacy classes. These classes are indexed by pairs $(\tau, x)$, with $\tau$ as above and $x$ in a product of two square class groups, for which a model exists. Each term is a product of local constants at $\Sigma$, $c(\tau)$, $m(\tau)$ and a product $n_L(x)$ of local counts. The existence of a model is a condition on the square classes. The sum of $n_L(x)$ over $x$ gives $\tfrac12(n_S(\tau) + e\, n_K(\tau))$ by the base point proposition, times the number of a finite set of square classes. A $\tau$ that is not integral off $\Sigma$ contributes zero. $\square$

**Theorem 8.12.7 (Trace identity).** Let the transfer data be valid and let $x_0$ be a finite adele of $D^\times$ that is 1 at $\Sigma$. There are finite adeles $x_0, x_1, \dots, x_n$, all 1 at $\Sigma$, and reals $a > 0$ and $b$ such that for all spaces $B_G$, $B_{S,i}$ (at $x_i$) and $B_K$ as above and each $t$ in the cone,
$$\begin{aligned} \operatorname{tr}\bigl(R_\theta(f_G^t) \mid B_G\bigr) = {} & a \sum_{i=0}^n \operatorname{tr}\bigl(R(f_S^{t,x_i}) \mid B_{S,i}\bigr) \\ & + b\, \operatorname{tr}\bigl(R(f_K^t) \mid B_K\bigr). \end{aligned}$$

Lean: `UpperTheory.V.Z.Sym.Glob.tFId0`.

*Proof.* By the unitary side, the left side is $c_G(\Sigma_S + e\,\Sigma_K)$. The trace formula on $D^1$ gives adeles $x_0, \dots, x_n$ such that the sum of the $D^1$ traces is $c_S \Sigma_S$ with $c_S > 0$. The trace formula on $D^\times$ gives $c_K \Sigma_K$ with $c_K > 0$. Take $a = c_G / c_S$ and $b = c_G e / c_K$. $\square$

The trace identity needs the local test functions at $\Sigma$ to have the right properties. The last result checks this.

**Proposition 8.12.8 (Validity of the local data).** Let $k$ be a nonarchimedean local field with $2 \ne 0$, let $\Delta = s^2$ with $s \ne 0$, and let $\chi$ be unramified. Then the local data at $k$ have open levels of finite index, positive local constants, and test functions with the required support, eigenvalue and orbital integral properties for each $t$ in the cone. Consequently, source transfer data with the conditions of validity give valid transfer data, with the level on $U_3$ and on $D^\times$ equal to the product of the local levels, and $\chi_v = |\cdot|_v$ at $v \in \Sigma$.

Lean: `UpperTheory.V.Z.Sym.Sig.sigMain` (also `UpperTheory.V.Z.Sym.So.datOk`, the global consequence).

*Proof.* The local statement collects facts about the level, the constants and the test functions on each of the three groups. The global statement applies it at each $v \in \Sigma$. At $v \in \Sigma$ the character $\chi_v$ is unramified and takes the value $q_v^{-1}$ at a uniformizer, so it is $|\cdot|_v$. Off $\Sigma$ the levels are the maximal compact subgroups. $\square$

**Remark 8.12.9 (Formalization).** The base point proposition is in [BasePt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/ScalarTuples/BasePt.lean#L274) and the local count in [EvUnit.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/LocalHermitianForms/LocalOrbitCounts/EvUnit.lean#L36), whose name says nothing about $\kappa$. The Hasse norm theorem enters as a named published statement `HasseNormSt` in [GlobNegOne.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GlobalUnitaryForms/ScalarTuples/GlobNegOne.lean#L54). The statement `SideG` leaves the sign $e$ free, but the proof gives $e = (-1)^{[F:\mathbb{Q}]}$, so the sign of $b$ is known. The trace identity names no published trace formula. The local statement `sigMain` in [SigMain.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/SignatureIntegrality/SignatureTorusFixedPoints/SigMain.lean#L9) only assembles nineteen facts from six lemmas, and it uses the same constant `hcS` for two of them, and `datOk` in [LocalLevelOutsideSigma.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/GeneralizedEigenspaces/CharacterShapes/FiniteOrbits/LocalLevelOutsideSigma.lean#L132) is bookkeeping on top of it. We have not unfolded the orbit counts, the masses or the models.
