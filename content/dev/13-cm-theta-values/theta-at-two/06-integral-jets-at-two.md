---
title: Integral jets at the prime two
decls:
  - Formalism.L2.Th1.Top.integral_operator_two_orthogonal
  - GlobalTheory.ThLoc.LocJets.jets_two_of
  - GlobalTheory.ThLoc.LocJets.jetsTwo
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Integral jets at the prime two

The [last section](/entry/th0-two-cm/) proved that translates of the theta function of a half period have integral transport at $2$, in the formal parameter of a curve with good reduction. Here we move this result to the coordinate $z$ of $\mathbb{C}$. In the coordinate $z$ the coefficients are not integral, but the derivatives at $0$ are. Then we apply the result to the theta function of a hermitian lattice in several variables with complex multiplication, through its fourth tensor power and a change of frame. The final theorem is used by the [local jet theorem](/entry/loc-jets-all/).

**Definition 8.6.1 (Jets).** Let $K$ be a field with an absolute value, and let $f = \sum_\kappa f_\kappa X^\kappa$ be a power series in variables $X_i$, $i \in I$, with $I$ finite. For a multi-index $\kappa$ put $\kappa! = \prod_i \kappa_i!$. The *jets* of $f$ are the numbers $\kappa! f_\kappa$; if $f$ is the Taylor series of a function at $0$, they are its partial derivatives at $0$. The series $f$ has *integral jets* if $|\kappa! f_\kappa| \leq 1$ for all $\kappa$. For a subring $R$ of $K$, $f$ has *jets in $R$* if $\kappa! f_\kappa \in R$ for all $\kappa$. For a polynomial $P = \sum_\kappa P_\kappa X^\kappa$ put $\langle P, f \rangle = \sum_\kappa P_\kappa \, \kappa! \, f_\kappa$.

For a function $f$ holomorphic near $0 \in \mathbb{C}^n$ and a field isomorphism $\iota : \mathbb{C} \to \mathbb{C}_p$, we write $\iota_* f \in \mathbb{C}_p[[X_i]]$ for the image under $\iota$ of the Taylor series of $f$ at $0$. For a lattice $L$ and $s \in \mathbb{C}$ we write $U_s f(z) = f(z + s) \exp(-\pi H(z, s) - \pi H(s, s)/2)$, with $H(z, w) = z \bar w / A$ as before.

**Lemma 8.6.2 (Jets through an exponential).** Let $K$ be a field of characteristic $0$ and $R$ a subring of $K$. Let $l$ and $l^{-1}$ be inverse power series with constant term $0$, and assume that the derivative $l'$ has constant term $1$ and coefficients in $R$. Let $G$ be a power series with coefficients in $R$ in finitely many variables $X_i$. Then $G(l^{-1}(X_i))$ has jets in $R$.

Lean: `Formalism.L2.Th1.G.jetsIn_toZ`.

*Proof.* Put $E = l^{-1}$ and $u = 1/l'$. Then $u$ has coefficients in $R$, and $E' = u(E)$. By induction $E^{(k)} = u_k(E)$ with $u_1 = u$ and $u_{k+1} = u_k' u$, all with coefficients in $R$. So $E^{(k)}(0) = u_k(0) \in R$: the series $E$ has jets in $R$. By the Leibniz rule, products of series with jets in $R$ have jets in $R$. So each term $G_\mu \prod_i E(X_i)^{\mu_i}$ has jets in $R$. It is divisible by $X^\mu$, so the sum over $\mu$ converges coefficientwise and has jets in $R$. $\square$

**Theorem 8.6.3 (Integral jets of translates).** Let $d \in \mathbb{N}$ with $d \equiv 7 \pmod 8$, and let $L$ be a lattice with $\omega_d L \subseteq L$. Let $\iota : \mathbb{C} \to \mathbb{C}_2$ be a field isomorphism and $W$ a Weierstrass curve over $\mathbb{C}_2$, uniformized by $L$ through $\iota$, with good reduction and $|a_1| = 1$. Let $\omega_0 \in L$ with $\omega_d \omega_0/2 \notin L$ and $\bar\omega_d \omega_0/2 \notin L$. Let $I$ and $\kappa$ be finite sets, $r : \kappa \to \mathbb{C}_2$ with $|r_k| \leq 1$, $s : \kappa \times I \to \mathbb{C}$, and $N > 0$ odd with $N s_{k,i} \in L$ for all $k, i$. Put
$$
\Theta_Z = \sum_{k \in \kappa} r_k \prod_{i \in I} \iota_*\big(U_{s_{k,i}} \theta_{\omega_0/2}\big)(X_i) .
$$
Then $\Theta_Z$ has integral jets, and $|\langle P, \Theta_Z \rangle| \leq 1$ for every polynomial $P$ over $\mathbb{C}_2$ with coefficients of absolute value at most $1$.

Lean: `Formalism.L2.Th1.Top.integral_operator_two_orthogonal`.

*Proof.* Let $f^{\iota}$ denote the transport of the last two sections. By item 3 of the [theorem for complex multiplication](/entry/th0-two-cm/), each $T_{k,i} = (U_{s_{k,i}} \theta_{\omega_0/2})^{\iota}$ has coefficients of absolute value at most $1$. So $G = \sum_k r_k \prod_i T_{k,i}(X_i)$ has integral coefficients. Since $W$ has good reduction, the invariant differential $l_W'(X) \, dX$ has integral coefficients and $l_W'(0) = 1$ (Silverman, Ch. IV, §1). By definition $f^{\iota} = (\iota_* f)(l_W)$, so $\iota_* f = f^{\iota}(l_W^{-1})$, and $\Theta_Z = G(l_W^{-1}(X_i))$. The last lemma, with $R$ the unit ball of $\mathbb{C}_2$, gives integral jets. Then each term $P_\kappa \cdot \kappa! (\Theta_Z)_\kappa$ of $\langle P, \Theta_Z \rangle$ has absolute value at most $1$, and so has the finite sum. $\square$

We now set up the hermitian data. Fix integers $a_0 > 0$, $b_0$, $c_0$ and $d > 0$ with
$$
4 a_0 c_0 = b_0^2 + d, \qquad a_0 \text{ odd}, \qquad d \equiv 7 \pmod 8, \qquad d \text{ prime},
$$
and $\lambda \in \mathbb{C}$, $\lambda \neq 0$. Put $\vartheta = (b_0 + \sqrt{-d})/2$, $L = \lambda(\mathbb{Z} a_0 + \mathbb{Z} \vartheta)$ with covolume $A$, and $\omega_0 = \lambda a_0$.

**Definition 8.6.4 (Hermitian theta data).** Let $I$ be a finite set and $h$ an $I \times I$ complex matrix, with form $H_h(z, w) = \sum_{i,j} z_i h_{ij} \bar w_j$ on $\mathbb{C}^I$. For a subgroup $\Lambda \subseteq \mathbb{C}^I$, the dual is $\{x : \operatorname{Im} H_h(x, y) \in \mathbb{Z} \text{ for all } y \in \Lambda\}$, and $\Lambda$ is *self-dual* if it equals its dual. Put $U_x F(z) = F(z + x) \exp(-\pi H_h(z, x) - \pi H_h(x, x)/2)$ and $\alpha(x) = \exp(\pi i \tfrac{\sqrt d}{2} \operatorname{Re} H_h(x, x))$. A *theta function* for $(h, \Lambda)$ is an entire function $\theta$ on $\mathbb{C}^I$ with $\alpha(x) U_x \theta = \theta$ for all $x \in \Lambda$.

On $\mathbb{C}^{4 \times I}$ we have the form $H_4$ of $h$ on each of the four blocks, and the standard form $H_L(y, y') = A^{-1} \sum_w y_w \bar y'_w$ with the lattice $L^{4 \times I}$. Let $g$ be a $\mathbb{C}$-linear automorphism of $\mathbb{C}^{4 \times I}$ with $H_L(gx, gy) = H_4(x, y)$, and put $\Lambda' = g(\Lambda^4)$ and $\Lambda'' = \Lambda' \cap L^{4 \times I}$. With $U$ and $\beta$ formed from $H_L$ as above, and $F_0(z) = \prod_w \theta_{\omega_0/2}(z_w)$, the *kernel* of $g$ is
$$
K_g(z) = [\Lambda' : \Lambda'']^{-1/2} \sum_{c \in \Lambda'/\Lambda''} \beta(c) \, U_c F_0(g z) .
$$
Let $p$ be a prime and $\iota : \mathbb{C} \to \mathbb{C}_p$ a field isomorphism. A *local normalization* of $\theta$ at $p$ is a pair $(g, \varepsilon)$, with $g$ as above and $\varepsilon \in \mathbb{C}$, such that $p \nmid [\Lambda' : \Lambda'']$, $[L^{4 \times I} : \Lambda'']$ is finite, $|\iota(\varepsilon)| \leq 1$, and $\prod_{a=1}^4 \theta(z_a) = \varepsilon K_g(z)$.

For such $g$, let $\gamma = \iota(g^{-1})$ be the matrix of $g^{-1}$ with $\iota$ applied to its entries. For a series $T$ in variables indexed by $I$, write $T^{\otimes 4}$ for $\prod_a T(X_{a,\cdot})$ in four blocks of variables.

**Lemma 8.6.5 (Fourth power).** Let $h$ and $\Lambda$ be as above with $\Lambda$ self-dual and $\vartheta \Lambda \subseteq \Lambda$, and $\theta$ a theta function for $(h, \Lambda)$. Let $(g, \varepsilon)$ satisfy the conditions of a local normalization at $p$. Let $t \in \mathbb{C}^I$ and $N > 0$ with $p \nmid N$ and $N t \in \Lambda$. Then there are a finite set $\kappa$, $r : \kappa \to \mathbb{C}_p$ with $|r_k| \leq 1$, $s : \kappa \to \mathbb{C}^{4 \times I}$ and $N' > 0$ with $p \nmid N'$ and $N' s_{k,w} \in L$, such that $(\iota_* U_t \theta)^{\otimes 4}(\gamma Y) = \Theta_Z(Y)$, with $\Theta_Z$ formed as in the theorem above, with $\omega_0 = \lambda a_0$ and with $\mathbb{C}_p$ in place of $\mathbb{C}_2$.

Lean: `GlobalTheory.ThLoc.LocJets.fourth_power_theta`.

*Proof.* The function $(U_t \theta)^{\otimes 4}(g^{-1} y)$ equals $\varepsilon \, (U_u K)(y)$ with $u = g(t, t, t, t)$ and $K = K_g \circ g^{-1}$, since $g$ is an isometry. We have $U_u U_c = \exp(-\pi i \operatorname{Im} H_L(u, c)) U_{u+c}$, and $U_s F_0(y) = \prod_w U_{s_w} \theta_{\omega_0/2}(y_w)$ because $H_L$ is diagonal. So we take $s_c = u + c$ and $r_c = \iota(\varepsilon \, m^{-1/2} \beta(c) \exp(-\pi i \operatorname{Im} H_L(u, c)))$ with $m = [\Lambda' : \Lambda'']$. The square root of $m$ is a unit, since $p \nmid m$. The values $\beta(c)$ are $\pm 1$, and the exponential is a root of unity because $\Lambda'$ is self-dual and $N u \in \Lambda'$. Then $N' = m N$ works. $\square$

**Lemma 8.6.6 (Gram transfer).** Let $h$ and $\Lambda$ be arbitrary, $g$ an isometry as above, and $p \nmid [\Lambda' : \Lambda'']$. Let $J$ be finite and $v_j \in \mathbb{C}^I$ with $\omega v_j \in \Lambda$ for all $\omega \in L$ and $j \in J$. Then there are $D \in \mathbb{C}_p^{(4 \times I) \times (4 \times J)}$ and $q_0 \in \mathbb{C}_p^{(4 \times J) \times (4 \times J)}$ with entries of absolute value at most $1$, such that
$$
\begin{aligned}
\textstyle\sum_w \gamma_{(a,i),w} D_{w,(b,j)} &= \delta_{ab} \, \iota(v_{j,i}), \\
\textstyle\sum_w D_{w,x} D_{w,y} &= \delta_{x_1 y_1} \iota\big(A \, H_h(v_{x_2}, v_{y_2})\big) + \iota(\sqrt{-d}) \, q_0(x, y) .
\end{aligned}
$$

Lean: `GlobalTheory.ThLoc.LocJets.gram_transfer`.

*Proof.* Let $D_{\cdot,(b,j)} = \iota(g e_{b,j})$, where $e_{b,j}$ has $v_j$ in block $b$ and $0$ elsewhere. The first identity holds. For $\omega \in L$, $\omega g e_{b,j} \in \Lambda'$, so $m \omega g e_{b,j} \in L^{4 \times I}$ with $m$ as before. So each coordinate $c$ of $g e_{b,j}$ has $m c L \subseteq L$. Since $d$ is prime, the multipliers of $L$ are $\mathbb{Z}[\omega_d]$, so $m c = m' + n' \omega_d$ with integers $m', n'$. Then $|\iota(c)| \leq 1$, and $\iota(c) - \iota(\bar c) = \iota(\sqrt{-d}) \, n'/m$. The bilinear sum $\sum_w D_{w,x} D_{w,y}$ is $\iota$ of the hermitian sum $A \, H_L(g e_x, g e_y) = A \, H_4(e_x, e_y)$, plus $\iota(\sqrt{-d})$ times an integral term. $\square$

**Lemma 8.6.7 (Frame composition).** Let $K$ be a field with an ultrametric absolute value, $\gamma$, $D$, $V$, $B$, $\theta_0$, $q_0$ and $\Phi$ matrices and a scalar over $K$, with $D$, $q_0$ and $\Phi$ of entries at most $1$, $\sum_w \gamma_{(a,i),w} D_{w,(b,j)} = \delta_{ab} V_{ij}$ and $\sum_w D_{w,x} D_{w,y} = \delta_{x_1 y_1} B_{x_2 y_2} + \theta_0 q_0(x, y)$. Then there are $C$ and $q_1$ with entries at most $1$, $\sum_w \gamma_{(a,i),w} C_{w,(b,x)} = \delta_{ab} (V\Phi)_{ix}$ and $\sum_w C_{w,x} C_{w,y} = \delta_{x_1 y_1} (\Phi^{T} B \Phi)_{x_2 y_2} + \theta_0 q_1(x, y)$.

Lean: `Formalism.L2.Th1.GD.FrameCompose_proof`.

*Proof.* Put $C_{w,(b,x)} = \sum_j D_{w,(b,j)} \Phi_{jx}$ and $q_1(x, y) = \sum_{j,k} \Phi_{j x_2} q_0((x_1, j), (y_1, k)) \Phi_{k y_2}$. $\square$

**Lemma 8.6.8 (Fourth roots of jets).** Let $K$ be a field of characteristic $0$ with an ultrametric absolute value, $T$ a series in variables indexed by $I$, and $\gamma$ a $(4 \times I)$-square matrix. Assume $T^{\otimes 4}(\gamma Y)$ has integral jets. Let $M \in K^{I \times \nu}$ and $C \in K^{(4 \times I) \times (4 \times \nu)}$ with entries of $C$ at most $1$ and $\sum_w \gamma_{(a,i),w} C_{w,(b,x)} = \delta_{ab} M_{ix}$. Then $T(MY)$ has integral jets.

Lean: `GlobalTheory.ThLoc.LocJets.jets_linear`.

*Proof.* The substitution $Y = C Z$ keeps integral jets: by the multinomial formula, the jets of $f(CZ)$ are sums of jets of $f$ times polynomials in the entries of $C$ with integer coefficients. So $T^{\otimes 4}(\gamma C Z) = S^{\otimes 4}(Z)$ has integral jets, where $S = T(MY)$. Its coefficient at $(\kappa, \kappa, \kappa, \kappa)$ gives $|\kappa! S_\kappa|^4 \leq 1$. $\square$

**Theorem 8.6.9 (Integral jets at two).** Let $a_0, b_0, c_0, d, \lambda$ and $L$ be as above. Let $h$ be an $I \times I$ complex matrix, $\Lambda \subseteq \mathbb{C}^I$ self-dual with $\vartheta \Lambda \subseteq \Lambda$, and $\theta$ a theta function for $(h, \Lambda)$. Let $\iota : \mathbb{C} \to \mathbb{C}_2$ be a field isomorphism and $W$ a Weierstrass curve over $\mathbb{C}_2$, uniformized by $L$ through $\iota$, with good reduction and $|a_1| = 1$. Assume that $\theta$ has a local normalization at $2$. Let $\kappa$ be finite, $r : \kappa \to \mathbb{C}_2$ with $|r_k| \leq 1$, $t : \kappa \to \mathbb{C}^I$, and $N > 0$ odd with $N t_k \in \Lambda$. Let $J$ be finite, $v_j \in \mathbb{C}^I$ with $\omega v_j \in \Lambda$ for all $\omega \in L$, $\nu$ finite and $\Phi \in \mathbb{C}_2^{J \times \nu}$ with $|\Phi_{jx}| \leq 1$. Put $M_{ix} = \sum_j \iota(v_{j,i}) \Phi_{jx}$ and
$$
\Theta = \sum_k r_k \, (\iota_* U_{t_k} \theta)(M Y) .
$$
Then $\Theta$ has integral jets, and $|\langle P, \Theta \rangle| \leq 1$ for every polynomial $P$ over $\mathbb{C}_2$ with coefficients of absolute value at most $1$.

Lean: `GlobalTheory.ThLoc.LocJets.jetsTwo` (also `GlobalTheory.ThLoc.LocJets.jets_two_of`, a second name).

*Proof.* The integer $b_0$ is odd, and $d$ is squarefree with $d \equiv 3 \pmod 4$, so $\mathbb{Z}[\omega_d] = \mathbb{Z}[\vartheta]$ and $\omega_d L \subseteq L$. We have $\omega_0 \in L$. If $\omega_d \omega_0/2 = \lambda(m a_0 + n \vartheta)$, the imaginary parts give $n = a_0/2$, which is not an integer. So $\omega_d \omega_0/2 \notin L$, and in the same way $\bar\omega_d \omega_0/2 \notin L$. Let $(g, \varepsilon)$ be the local normalization. The Gram transfer gives $D$ and $q_0$, and frame composition with $V_{ij} = \iota(v_{j,i})$ and the matrix $\Phi$ gives $C$ with $\gamma C$ block diagonal with blocks $M$. Fix $k$. The fourth power lemma for $t_k$ writes $(\iota_* U_{t_k} \theta)^{\otimes 4}(\gamma Y)$ as a series $\Theta_Z$, and the theorem on translates, with $4 \times I$ in place of $I$, shows that it has integral jets. The lemma on fourth roots gives integral jets for $(\iota_* U_{t_k} \theta)(MY)$. A sum of such series times $r_k$ has integral jets, and the bound on $\langle P, \Theta \rangle$ follows as before. $\square$

**Remark 8.6.10 (Formalization).** The theorem on translates uses only the integrality in item 3 of [ThetaZeroTwoComplexMult.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/FrobeniusFibreCurves/LogarithmicSubstitution/ThetaZeroTwoComplexMult.lean#L102); the unit coefficient of item 3 and items 1 and 2 are not used. Its name speaks of an orthogonal integral operator, but no orthogonality appears. The proofs of `fourth_power_theta` and `gram_transfer` were not unfolded; the arguments above are the classical ones. The proof of frame composition is the one given. In [FourthPowerTheta.lean](lean:Development/AbelianVarietyTheory/Definitions/GaloisGeometry/FourthPowerTheta.lean#L262) the proof discards the Gram relation that frame composition returns, so at $2$ the Gram relation is needed only as an input to frame composition. The theorem modules sit in a folder named `Definitions`. The lemma on exponentials has a second copy, `jetsIn_toZ` in the namespace `GramFrameCompositionTwoFacts`, in [ThetaZeroJetsCurveHolds.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/RamifiedCurveKernels/PairedSquareJets/ThetaZeroJetsCurveHolds.lean#L202). An unrelated declaration `jetsTwo` with a different statement exists in the elliptic torsion files.
