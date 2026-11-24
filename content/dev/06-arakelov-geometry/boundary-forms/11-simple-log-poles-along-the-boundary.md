---
title: Simple log poles along the boundary
decls:
  - GlobalTheory.LogPole.exists_kodaira_spencer_comparison_log_pole
  - GlobalTheory.T.kodaira_spencer_comparison_along_boundary
  - GlobalTheory.LogPole.exists_log_pole_along_boundary
  - GlobalTheory.LogPole.log_pole_along_boundary_is_simple
  - GlobalTheory.T.exists_simple_log_pole_along_boundary
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Simple log poles along the boundary

On a toroidal compactification of a Shimura variety the canonical bundle and an automorphic line bundle are related through the boundary divisor $D$: the automorphic bundle of the canonical weight $\kappa$ is the bundle of top forms with logarithmic poles along $D$, $L(\kappa) \cong \Omega^n(\log D)$ ([Mumford's proportionality theorem](/learn/abelian-varieties/#mumfords-proportionality-theorem)). So a top form on the interior that corresponds to a section of $L(\kappa)$ has at most a simple pole along $D$. This section proves this in the local form that is needed in [the next section](/entry/log-canonical-refl-of-boundary/), where it turns cusp forms into regular top forms on a resolution. The proof compares the log Kodaira-Spencer map on the boundary charts with the Kodaira-Spencer map of the deformation theory, up to one nonzero rational constant.

We fix a family that satisfies the hypotheses of the second kind, a level and a coefficient field $F$. Let $Y$ be the toroidal flag model, $Z$ a component, and $Y_0$ the toroidal flag space over $X_0$ of [the section on separating orbits](/entry/separate-orbits-by-cusp/). Let $U_0 \subset Y_0$ be the interior, the preimage of the open Shimura variety, and let the boundary be its complement. Let $n$ be the dimension of $Y_0$ (the dimension of the flag space) and let $\kappa$ be the canonical weight of the datum. Write $K_{Y_0}$ for the canonical bundle of $Y_0$. A *canonical identification* is a section $\omega_0$ of $K_{Y_0} \otimes L_0(\kappa)^{-1}$ over the interior; through it a section of $L_0(\kappa)$ on $U_0$ becomes a top form on $U_0$ ([the Kodaira-Spencer map](/learn/abelian-varieties/#the-kodaira-spencer-map)).

**Definition 2.11.1 (Log Kodaira-Spencer comparison).** Let $s \in \mathbb{Q}$. The toroidal model satisfies the *log Kodaira-Spencer comparison with constant* $s$ if the following holds. Let $U$ be an affine open subset of the base of the compactification, let $e$ be a basis of the Lie algebra over $U$ by eigenvectors of $\mathcal{O}_E$, and let $D$ be a logarithmic derivation of $U$ that preserves the ideal of the boundary. Let $\Theta = (\Theta_{a b})$ be the log Kodaira-Spencer matrix of $D$ in the basis $e$. Then, for every framed point $y$ over a field $K$ that lies in $U$ and carries a frame of the base, and every first order deformation of $y$ along $D$, the Kodaira-Spencer map of the deformation has, in the row of a pair $(\tau, k_2)$ and the column of $(\bar\tau, k_1)$, the entry
$$s \cdot \Theta\bigl(e_{\tau, k_2}, e_{\bar\tau, k_1}\bigr)(y).$$

So the comparison says that two descriptions of the same tangent direction agree up to the factor $s$: one through the log structure of the boundary chart, the other through deformations of the abelian scheme with its $\mathcal{O}_E$-action.

**Theorem 2.11.2 (Kodaira-Spencer comparison along the boundary).** Assume the hypotheses of the second kind. Then there is $s \in \mathbb{Q}$ with $s \ne 0$ such that every toroidal model satisfies the log Kodaira-Spencer comparison with constant $s$.

Lean: `GlobalTheory.LogPole.exists_kodaira_spencer_comparison_log_pole` (also `GlobalTheory.T.kodaira_spencer_comparison_along_boundary`, a second name).

*Proof.* The Čech description of the Kodaira-Spencer class gives one constant: there is $s \ne 0$ in $\mathbb{Q}$ such that, for every deformation glued from a Čech cocycle of derivations, the Kodaira-Spencer value of the deformation is $s$ times the value of the cocycle on the Hodge filtration. Fix $U$, $e$, $D$, $\Theta$, a framed point $y$ over $K$ and a deformation along $D$. The compatibilities of the Kodaira-Spencer map give the data of the deformation over the dual numbers $K[\varepsilon]$: the deformed abelian scheme, its Hodge filtration, the polarization and the frames, compatible with $y$. The log Kodaira-Spencer matrix $\Theta$ gives a Čech cocycle that glues this deformation, so the Čech constant applies, with $\Theta$ evaluated at $y$. The matrix $\Theta$ vanishes outside the blocks of conjugate pairs $(\tau, \bar\tau)$, by the $\mathcal{O}_E$-linearity of the polarization. On these blocks the identity on the Hodge filtration, read row by row, is the entry formula of the definition. The field $K$ has characteristic $0$ because it is an extension of $F$. $\square$

The constant $s$ is the same for all models and points. In the local computation below only $s \ne 0$ is used.

**Theorem 2.11.3 (The canonical identification has a log pole).** Assume the hypotheses of the second kind, let $F$ be algebraically closed in the function field, and assume that the Kodaira-Spencer map of the flag space is an isomorphism at every framed point over every field extension of $F$. Assume that $Y_0$ is a variety and that $U_0$ is dense in it, and let $\omega_0$ be a canonical identification. Let $y \in Y_0$ and let $V$ be an open neighbourhood of $y$. Then there are an open neighbourhood $W \subset V$ of $y$, contained in a trivializing chart of the canonical bundle and in a chart of the automorphic bundles, and sections $\delta, u$ of $\mathcal{O}_{Y_0}$ over $W$ such that:

1. $u$ is a unit on $W$;
2. for $z \in W$, the germ of $\delta$ at $z$ is a unit if and only if $z \in U_0$;
3. on every open $W' \subset W$, the germ of $\delta$ divides the germ of every function that vanishes at all points of $W'$ outside $U_0$;
4. at every point $z$ of $W \cap U_0$ with values in a field, $\delta(z) \, \omega_0(z) = u(z)$ in the charts.

Lean: `GlobalTheory.LogPole.exists_log_pole_along_boundary`.

So $\delta$ is a local equation of the reduced boundary, and $\delta \omega_0$ extends to a nowhere vanishing section over $W$: the identification has at most a simple pole along the boundary.

*Proof.* Near $y$ choose a basis $e$ of the Lie algebra by $\mathcal{O}_E$-eigenvectors on an affine open set $U$ of the base, and a big cell chart of the flag space over it, with coordinates $L$ for the vertical directions. Choose logarithmic vector fields $b_1, \dots, b_m$ on $U$ that form a symmetric basis for the log Kodaira-Spencer pairing, and coordinates $x_1, \dots, x_m$ on $U$ such that the determinant $\det b(x)$ of the matrix $(b_i(x_j))$ vanishes exactly on the boundary to order one. Put $\delta$ equal to the pullback of $\det b(x)$ to $Y_0$. The base coordinates together with the vertical coordinates form an étale chart of $Y_0$, so their differentials give a frame of the canonical bundle with a unit Jacobian $J$ against the chart of $K_{Y_0}$.

Now take the constant $s$ of the previous theorem. With the assumption that the Kodaira-Spencer map is an isomorphism, the comparison shows that the determinant of the log Kodaira-Spencer map in the bases $b$ and $e$ is a nonzero rational multiple $a$ of the horizontal part of $\omega_0^{-1}$. The Kodaira-Spencer matrix has a block form for the splitting of the tangent space into the horizontal and the vertical parts, and the vertical block has determinant $1$ in the chosen coordinates. So, on the interior, $\delta \, \omega_0$ equals $a$ times a diagonal unit times $J$, and $u = a \cdot (\text{diagonal unit}) \cdot J$ is a unit on $W$. Properties 2 and 3 hold because $\det b(x)$ is a reduced equation of the boundary on $U$. $\square$

The second theorem removes the choice of $\delta$: every reduced equation of the boundary does the same.

**Theorem 2.11.4 (The log pole is simple).** Assume the hypotheses of the first theorem, together with Grothendieck's deformation theory. Let $y \in Y_0$ be a point outside $U_0$, let $V$ be an open neighbourhood of $y$ and $t$ a section of $\mathcal{O}_{Y_0}$ over $V$ such that the germ of $t$ at $z \in V$ is a unit exactly when $z \in U_0$, and such that the germ of $t$ divides the germ of every function on an open $W \subset V$ that vanishes at the points of $W$ outside $U_0$. Then there are an open neighbourhood $V' \subset V$ of $y$, inside a chart of the canonical bundle and of the automorphic bundles, and a section $u$ over $V'$ whose germs are units, such that $t \, \omega_0 = u$ at every point of $V' \cap U_0$.

Lean: `GlobalTheory.LogPole.log_pole_along_boundary_is_simple` (also `GlobalTheory.T.exists_simple_log_pole_along_boundary`, a second name).

*Proof.* Take $W$, $\delta$ and $u$ from the previous theorem. The local ring of $Y_0$ at $y$ is normal, hence a domain. Both $t$ and $\delta$ are equations of the reduced boundary near $y$: each vanishes at the boundary points, so each divides the other. In a domain, two elements that divide each other differ by a unit, so $t = b \delta$ with $b$ a unit near $y$. On a smaller neighbourhood $V'$ the section $b$ is a unit, and $t \, \omega_0 = b \, \delta \, \omega_0 = b u$. Equality at the points with values in fields gives equality of germs, so we may take $u' = b u$. $\square$

**Remark 2.11.5 (Formalization).** In the theorem that the log pole is simple, the assumption of Grothendieck's deformation theory and the assumption $y \notin U_0$ are introduced as `_` and never used ([ExistsSimpleLogPoleAlongBoundary.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ExistsSimpleLogPoleAlongBoundary.lean#L136)). The rational constant $a$ comes from `logKodairaSpencer_det_eq_const_mul_horizontal` (line 44). The same two statements appear again, under the names `exists_pole` and `simple_pole` with a different list of hypotheses, in `KodairaSpencerCanonicalDivisor.lean` (lines 124 and 240). We have not unfolded `CanId` beyond its section $\omega_0$, nor `KSIso` and `IsVariety₀`; the descriptions above are by name and by their use. The constant $s$ comes from `cech_kodaira_spencer_class_constant` (ExistsConstantCechKodairaSpencerValue.lean, line 56), whose proof we did not read.
