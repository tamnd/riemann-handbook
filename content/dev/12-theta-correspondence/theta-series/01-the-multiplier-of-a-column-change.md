---
title: The multiplier of a column change
decls:
  - GlobalTheory.Phase.Mult.isMu_multiplier_sq_mul_det
  - GlobalTheory.T.multiplier_sq_mul_det_unitary_column_change
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The multiplier of a column change

This section attaches Siegel theta series to the points of a unitary period domain and proves one arithmetic fact about them. Let $h$ be a unitary $n \times n$ matrix over a CM field. If moving the columns of the variable by $h$ turns one theta series into $t$ times another, then $t^2$ times a product of conjugates of $\det h$ is a root of unity. The next section uses this at each complex point of a moduli space, and so shows that a change of representative multiplies the short theta values by a root of unity.

### Theta series on frames

Let $E$ be a CM field with complex conjugation $a \mapsto \bar a$ and ring of integers $\mathcal{O}_E$. A *CM type* is a set $\Psi$ of embeddings $E \to \mathbb{C}$ such that, for each embedding $\tau$, exactly one of $\tau$ and $\bar\tau$ lies in $\Psi$. For a matrix $G \in M_r(E)$ with $\bar G^T = G$ we write $h_G(u, v) = \sum_{a,b} u_a G_{ab} \bar v_b$ for $u, v \in E^r$. This is a [[Hermitian form|8NJ7XY6F1S]], as in [Hermitian and skew-Hermitian forms](/learn/algebra/#hermitian-and-skew-hermitian-forms).

**Definition 3.1.1 (Unitary period data).** A *unitary period datum* of rank $r$ consists of a CM field $E$ with a CM type $\Psi$, an invertible Hermitian matrix $G \in M_r(E)$ that has signature $(p_0, r - p_0)$ at each $\tau \in \Psi$, a finitely generated $\mathcal{O}_E$-lattice $\Lambda \subset E^r$ that spans $E^r$, and an element $\kappa_0 \in E$ with $\bar\kappa_0 = -\kappa_0$ and $\operatorname{Im} \tau(\kappa_0) < 0$ for $\tau \in \Psi$. The datum also has an arithmetic subgroup and a weight character, which this section does not use. The *symplectic form* of the datum is
$$\langle u, v \rangle = \operatorname{Tr}_{E/\mathbb{Q}}\big(-\tfrac{\kappa_0}{2}\, h_G(u, v)\big) \in \mathbb{Q}.$$

A *frame* is a family $x = (x_\tau)_{\tau \in \Psi}$ of matrices $x_\tau \in M_r(\mathbb{C})$. Let $g_\tau(x)$ be the Gram matrix $\big(h_{\tau(G)}(x_{\tau,a}, x_{\tau,b})\big)_{a,b}$ of the columns of $x_\tau$, and let $\epsilon_i = \prod_{a < i} \epsilon(a)$ with $\epsilon(a) = 1$ for $a < p_0$ and $\epsilon(a) = -1$ otherwise (columns counted from 0). The *period domain* $\mathcal{D}$ is the set of frames with $\det x_\tau \ne 0$ and $\epsilon_i \operatorname{Re} \det\big(g_\tau(x)\big)_{a, b < i} > 0$ for all $\tau \in \Psi$ and $0 \le i \le r$. So the first $p_0$ columns span a positive subspace and the others a negative one. For $v \in E^r$ and a pair $(\tau, a)$ with $\tau \in \Psi$ and $1 \le a \le r$, the *period* of $v$ is $h_{\tau(G)}(x_{\tau, a}, \tau(v))$, the pairing with column $a$, if $a \le p_0$, and the $a$-th coordinate of $x_\tau^{-1} \tau(v)$ if $a > p_0$.

Assume that $\Lambda$ has a *symplectic basis*: an isomorphism $b \colon \mathbb{Z}^{2g} \to \Lambda$ with $\langle b_i, b_j \rangle = -\omega(i, j)$, where $\omega$ is the standard symplectic form on $\mathbb{Z}^{2g}$. Fix a bijection $i \mapsto (\tau_i, a_i)$ from $\{1, \dots, g\}$ to $\Psi \times \{1, \dots, r\}$. For a frame $x$ let $\Omega_1(x)$ and $\Omega_2(x)$ be the $g \times g$ matrices of periods of the first $g$ and the last $g$ basis vectors. Put
$$A(x) = \Omega_1(x)^{-1}, \qquad \tau(x) = \Omega_1(x)^{-1} \Omega_2(x).$$
This is the usual normalization of a period matrix of the complex torus that $x$ defines on $\Lambda \otimes \mathbb{R}$, as in [the transformation formula](/learn/theta-functions-cm/#the-transformation-formula).

**Definition 3.1.2 (Schwartz-Bruhat functions and theta series).** A function $\varphi$ on $M_{n \times g}(\mathbb{Q})$ is *Schwartz-Bruhat* if there is an integer $R > 0$ such that $\varphi(x) \ne 0$ implies that $R x$ is integral, and $\varphi(x + R y) = \varphi(x)$ for all integral $y$. For $\tau$ in the Siegel upper half space $\mathbb{H}_g$ and $\zeta \in (\mathbb{C}^g)^n$, the *Siegel [[theta series|2F5CYQJVAF]]* of $\varphi$ is
$$\theta_\varphi(\tau, \zeta) = \sum_{x \in M_{n \times g}(\mathbb{Q})} \varphi(x)\, \exp\Big(\pi i \sum_{k=1}^n \big(x_k^T \tau x_k + 2\, x_k^T \zeta_k\big)\Big),$$
with $x_k$ the $k$-th row of $x$. The *theta series on frames* is, for $x \in \mathcal{D}$ and $z \in (\mathbb{C}^g)^n$,
$$\Theta_\varphi(x, z) = \det A(x)^{n/2} \exp\Big(\tfrac{\pi}{2} \sum_k (A z_k)^T (\operatorname{Im} \tau)^{-1} (A z_k)\Big)\, \theta_\varphi\big(\tau(x), A z\big),$$
with $A = A(x)$ and $\tau = \tau(x)$. The first two factors are the usual automorphy factors that make $\Theta_\varphi$ a function of the frame.

The Schwartz-Bruhat functions carry the [[Heisenberg group|ZZYCV5EX9J]] action of the Schrödinger model of [the Weil representation](/learn/theta/#the-schrdinger-model). For $a, b \in M_{n \times g}(\mathbb{Q})$,
$$(\rho(a, b)\varphi)(x) = \varphi(x - b)\, \exp\Big(\pi i \sum_k (2\, x_k \cdot a_k - a_k \cdot b_k)\Big).$$
For $y \in M_{n \times r}(E)$ we write $\rho(y)$ for $\rho(a, b)$, where $(a, b)$ are the coordinates of the rows of $y$ in the basis $b$. The inner product $\langle \varphi, \psi \rangle$ is the normalized sum of $\varphi \bar\psi$ over a period, that is, the Haar integral on $M_{n \times g}(\mathbb{A}_f)$ in disguise.

**Definition 3.1.3 (Vacuum vectors).** Let $w \in E$ be integral with $w + \bar w = 1$, and put $\varepsilon_w(y) = \exp(\pi i \sum_k \langle y_k, w y_k \rangle)$. For a subgroup $A \subset M_{n \times r}(E)$, a *vacuum* for $A$ is a Schwartz-Bruhat function $\varphi$ with $\langle \varphi, \varphi \rangle = 1$ and $\varepsilon_w(y) \rho(y) \varphi = \varphi$ for all $y \in A$. The *projection* $P_A \varphi$ is the average of the distinct functions $\varepsilon_w(y)\rho(y)\varphi$, $y \in A$, and $u(\varphi) = \langle \varphi, \varphi \rangle^{-1/2} \varphi$ is the normalization.

For an $\mathcal{O}_E$-lattice $\Lambda_0 \subset E^n$ and a lattice $L \subset E^r$, let $\Lambda_0 \otimes L$ be the subgroup of $M_{n \times r}(E)$ generated by the matrices $v u^T$, $v \in \Lambda_0$, $u \in L$. A lattice $L \subset E^r$ is *self-dual* if it is finitely generated and $L = \{ x : \langle x, y \rangle \in \mathbb{Z} \text{ for all } y \in L \}$. Let $V_n$ be the set of finitely generated $\mathcal{O}_E$-lattices $\Lambda_0 \subset E^n$ that are self-dual for the standard form $\sum_k u_k \bar v_k$ and commensurable with $\mathcal{O}_E^n$ (the unimodular Hermitian lattices of [lattices in Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces)).

**Definition 3.1.4 (Column action).** For $1 \le i \le g$ let $\sigma_i = \bar\tau_i$ if $a_i \le p_0$ and $\sigma_i = \tau_i$ if $a_i > p_0$. A matrix $h \in M_n(E)$ is *unitary* if $\bar h^T h = 1$. It acts on $z \in (\mathbb{C}^g)^n$ by
$$(h \cdot z)_{k, i} = \sum_{k'} \sigma_i(h_{k k'})\, z_{k', i}.$$

So $h$ mixes the $n$ rows of $z$, through the embedding $\sigma_i$ in the column $i$. A complex number $c$ is a *root of unity* if $c^m = 1$ for some $m > 0$.

### The theorem

**Theorem 3.1.5 (Multiplier of a column change).** Let a unitary period datum with a symplectic basis be given, and let $n$ be even. Let $w \in \mathcal{O}_E$ with $w + \bar w = 1$, let $h \in M_n(E)$ be unitary, let $\Lambda_1, \Lambda_2 \in V_n$, let $L \subset E^r$ be self-dual, and let $v$ be a vacuum for $\mathcal{O}_E^n \otimes L$. Put $\varphi_j = u(P_{\Lambda_j \otimes L}\, v)$ for $j = 1, 2$. Let $x \in \mathcal{D}$ and $t \in \mathbb{C}$ with $|t| = 1$, and assume
$$\Theta_{\varphi_2}(x, h \cdot z) = t\, \Theta_{\varphi_1}(x, z) \quad \text{for all } z.$$
Then $t^2 \prod_{i=1}^g \sigma_i(\det h)$ is a root of unity.

Lean: `GlobalTheory.Phase.Mult.isMu_multiplier_sq_mul_det` (also `GlobalTheory.T.multiplier_sq_mul_det_unitary_column_change`, a second name)

*Proof.* We use four facts that are proved in the sources of this chapter, and a fifth one stated below.

1. There is $u \in \mathbb{C}$ with $|u| = 1$ such that, for every $\Lambda_0 \in V_n$, the function $u(P_{\Lambda_0 \otimes L} v)$ is a vacuum for $\Lambda_0 \otimes L$, and every value of $u \cdot u(P_{\Lambda_0 \otimes L} v)$ has a root of unity as its phase: $c^m = |c|^m$ for some $m > 0$. The same $u$ serves all $\Lambda_0$.
2. There is a rational symplectic matrix $s = \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix} \in \mathrm{Sp}_{2ng}(\mathbb{Q})$ that fixes the block diagonal point $B = \operatorname{diag}(\tau(x), \dots, \tau(x)) \in \mathbb{H}_{ng}$. Its automorphy factor $D = \gamma B + \delta$ satisfies $\det D \cdot d = 1$, with $d = \prod_i \sigma_i(\det h)$, and $\zeta \mapsto \zeta D^{-1}$ is the action $z \mapsto h \cdot z$ written in the coordinates $\zeta_k = A(x) z_k$. This $s$ is the action of $h$ on $\Lambda \otimes \mathbb{Q}^n$ written in the symplectic basis.
3. $|d| = 1$, since $\sigma(\det h)\, \overline{\sigma(\det h)} = \sigma(\det h \cdot \overline{\det h}) = 1$ for each embedding $\sigma$.
4. The function $\varphi_2$ is not zero, since $\langle \varphi_2, \varphi_2 \rangle = 1$.

Write the hypothesis in the coordinates $\zeta = A(x) z$. The factors $\det A(x)^{n/2}$ cancel. Since $s$ fixes $B$, the quadratic form $(\operatorname{Im} B)^{-1}$ changes under $\zeta \mapsto \zeta D^{-1}$ by the term $-2i\, \zeta^T D^{-1} \gamma\, \zeta$. So the hypothesis becomes
$$\theta_{\varphi_2}(B, \zeta D^{-1}) = t\, e^{\pi i\, \zeta^T D^{-1} \gamma \zeta}\, \theta_{\varphi_1}(B, \zeta),$$
with the sum over the $n$ rows understood. The automorphy factor $\det D^{n/2}$ of the transformation law is defined only for an even number of rows, so we double. Let $\varphi^{(2)}(x_0, x_1) = \varphi(x_0)\varphi(x_1)$ on $M_{2 \times ng}(\mathbb{Q})$. Then $\theta_{\varphi^{(2)}}(B, (\zeta_0, \zeta_1)) = \theta_\varphi(B, \zeta_0)\theta_\varphi(B, \zeta_1)$, so the identity holds for $\varphi_j^{(2)}$ with $t^2$ in place of $t$.

The [[Weil representation|H3Q2703KKV]] of $s$ gives a Schwartz-Bruhat function $\omega(s)\varphi_1^{(2)}$ with the transformation law
$$\theta_{\omega(s)\varphi}(sB, \zeta D^{-1}) = \det D \cdot e^{\pi i \zeta^T D^{-1}\gamma \zeta}\, \theta_\varphi(B, \zeta).$$
It is built from the decomposition of $s$ into Siegel parabolic elements and the matrix $J$, as in [the transformation formula](/learn/theta-functions-cm/#the-transformation-formula). Since $sB = B$ and $\det D \cdot d = 1$, the two identities give
$$\theta_{\varphi_2^{(2)}}(B, \cdot) = \theta_{t^2 d\, \omega(s)\varphi_1^{(2)}}(B, \cdot).$$
A Schwartz-Bruhat function is determined by its theta series at one point of the Siegel space, since the theta series is a Fourier series in $\zeta$ whose coefficients are the values of the function times nonzero factors. Hence $\varphi_2^{(2)} = t^2 d\, \omega(s)\varphi_1^{(2)}$.

Multiply $\varphi_1$ and $\varphi_2$ by the common phase $u$ of fact 1. This multiplies both sides by $u^2$ and changes nothing. The values of $(u\varphi_1)^{(2)}$ have root of unity phases, and this function is a vacuum for a subgroup of $M_{2 \times ng}(\mathbb{Q})$. For a rational symplectic matrix and an even number of rows, the Weil transform keeps both properties. This is the fifth fact. Pick a point $y$ with $\varphi_2^{(2)}(y) \ne 0$, by fact 4. Then $t^2 d$ is a quotient of two complex numbers whose phases are roots of unity, so its phase is a root of unity. By fact 3 and $|t| = 1$ we have $|t^2 d| = 1$. A complex number of absolute value 1 whose phase is a root of unity is a root of unity. $\square$

**Remark 3.1.6.** The classical theta transformation formula says that for $\gamma \in \mathrm{Sp}_{2g}(\mathbb{Z})$ the theta constant $\theta(\gamma \tau)$ equals $\det(C\tau + D)^{1/2}\, \theta(\tau)$ up to an eighth root of unity (Mumford, *Tata Lectures on Theta I*, Chapter II; Igusa, *Theta Functions*, Chapter V). The theorem is a version of this fact for a rational symplectic matrix that fixes the point. Its content is that the multiplier is a root of unity, not its exact value.

**Remark 3.1.7 (Formalization).** The theorem is proved in [MultiplierSqMulDetUnitaryColumnChange.lean](lean:Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation/MultiplierSqMulDetUnitaryColumnChange.lean#L210). The core is the lemma `isMu_of_fixed` at line 51, which takes the symplectic matrix, the fixed point and the two phase statements as inputs. The four facts of the proof are the results `heisenbergVacuum_projection_rootOfUnity_phases`, `exists_rational_symplectic_unitary_columns`, `norm_det_unitary` and the normalization $\langle \varphi_2, \varphi_2 \rangle = 1$. The Weil operator comes from `exists_weil_of_symplectic`, and the phase property of its image from `rootOfUnityPhaseVacuum_siegelThetaTransform`. The wrapper `multiplier_sq_mul_det_unitary_column_change` proves the same statement by `first | exact ...`.
